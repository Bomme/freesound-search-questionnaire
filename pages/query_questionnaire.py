import random

import streamlit as st
from streamlit_extras.switch_page_button import switch_page


def construct_freesound_url(sound_id: str, user_id: str|int):
    prefix = sound_id[:len(sound_id) - 3]
    quality = "hq"
    return f"https://cdn.freesound.org/previews/{prefix}/{sound_id}_{user_id}-{quality}.mp3"


def toggle_session_state(key: str):
    if key not in st.session_state:
        st.session_state[key] = True
    else:
        st.session_state[key] = not st.session_state[key]


def clear_session_state():
    del st.session_state["query_submitted"]
    del st.session_state["sound_url"]


if "user_id" not in st.session_state:
    switch_page("welcome")

sounds = [
    (22041, 117199),
    (50809, 107780),
    (516639, 7724336),
    (467422, 2056667),
    (173314, 2168040),
    (374165, 2475994),
]

st.title("Freesound search questionnaire", anchor=False)

st.header("Listen to this sound", anchor=False)

st.warning(
    """
    🔊 Before pressing play, please make sure the volume of your headphones or speakers is set to a comfortable level. 
    """,
    icon="⚠️"
)

st.write("This is a random sound from Freesound.")

if "sound_url" not in st.session_state:
    s_id, user_id = sounds[random.randint(0, len(sounds) - 1)]
    st.session_state["sound_url"] = construct_freesound_url(str(s_id), str(user_id))

st.audio(st.session_state["sound_url"], format="audio/mp3", start_time=0)

st.subheader("How would you search for this sound?", anchor=False)

st.write("Imagine you are looking for sound like this in Freesound. What would you type into the search bar?")

query_submitted = "query_submitted" in st.session_state and st.session_state["query_submitted"]

with st.expander(
        label="📋 Instructions", expanded=not query_submitted
):
    st.write(
        """
        Write a query that you would use to search for this sound in Freesound.
        You can write anything you want, but try to be as specific as possible.
        
        🧠 Imagine you are looking for a sound like this to use in:
        ** a video game 
        ** a movie
        ** a podcast
        ** a song
        ** a presentation
        ** a website
        ** a theatre play
        ** ...
        
        ☝️ There are no other search filters available, so you can only use the search bar in this experiment.
        """
    )

with st.form("query_form", clear_on_submit=True, border=False):
    query = st.text_input("Please type your query here", disabled=query_submitted)
    st.form_submit_button("Submit", on_click=toggle_session_state, args=["query_submitted"], disabled=query_submitted, type="primary")
    skipped = st.form_submit_button("Skip", on_click=switch_page, args=["query_questionnaire"], disabled=query_submitted)

if skipped:
    del st.session_state["sound_url"]
    st.rerun()


if query and query_submitted:
    st.write(f"Your query: {query}")

    st.subheader("What's important for you in this sound?", anchor=False)
    st.write("Please select all that apply.")
    options = [
        "The **temporal order** of events in the sound",
        "The **pitch** of the sound",
        "The **timbre** of the sound",
        "The **duration** of the sound",
        "The **loudness** of the sound",
        "The **spatial** characteristics of the sound",
        "The **rhythm** of the sound",
        "The **texture** of the sound",
        "The **main sound source**",
        "The **usage** context of the sound",
        "The **perceived emotion** of the sound",
        "The **quality** of the sound",
            ]
    random.shuffle(options)
    with st.form("desc_form", clear_on_submit=True, border=False):
        # tags = st.multiselect(
        #     "In my query, I mention",
        #     options=options,
        #     help="Please select all that apply.",
        # )
        for option in options:
            st.checkbox(option)
        additional_aspects = st.text_input("Please add any aspects that are important to you but not listed above.")
        followup_submitted = st.form_submit_button("Submit", on_click=clear_session_state, type="primary")
