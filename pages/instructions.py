"""This file contains the instructions for the experiment."""

import streamlit as st

st.set_page_config(
    page_title="Sound search questionnaire",
    page_icon=":question:",
    initial_sidebar_state="collapsed",
)

st.title("Sound search questionnaire", anchor=False)
# st.info("Please read the instructions carefully before proceeding.")

st.header("Instructions", anchor=False)


# TODO add using text only
st.markdown(
    """
    🔎 In this experiment, you will be asked to search for sounds in a hypothetical sound library.
    
    🔠 You will only be able to use text to search for sounds. You will not be able to use any other search filters.
    
    🧠 Imagine a limitless system where you can find any sound in any way you can think of, using text only.
    
    📋 To guide your search, you will be given an example. The example will be either text or audio, depending on the task.
    
    🎯 Depending on the task, you will be asked to try to find *one* specific sound or as many sounds as you can.
    
    📝 After each search, you will be asked to answer a few questions about your choices.
    
    ❌ You will not actually perform the search. You will only imagine that you are searching for the sounds.
    
    🎧 Please use headphones or earphones to listen to the audio prompts.
"""
)

st.warning(
    """
    🔊 Before proceeding, please make sure the volume of your headphones or speakers is set to a comfortable level. 
    """,
    icon="⚠️",
)

# with st.expander("Still a bit unclear about what you need to do? Here's a quick summary:"):
# # st.header("More about the experiment", anchor=False)
#
#     st.markdown(
#             """
#             *Still a bit unclear about what you need to do? Here's a quick summary:*
#
#             ✍️ Write a query that you would use to search for a sound in an online sound library.
#             You can write anything you want, but try to be as specific as possible. After all, you really want to find the
#             sound you are looking for!
#
#             👨‍💻 Use common sense and your experience with search engines on the internet to guide your search.
#
#             🧠 If it helps, imagine you are looking for a sound to use in one of the following settings:
#             * a video game
#             * a movie
#             * a podcast
#             * a song
#             * a presentation
#             * a website
#             * a theatre play
#             * ... or anything else you can think of!
#
#             ☝️ There are no other search filters available, so you can only use the search bar in this experiment.
#             """
#     )

with st.form("Comprehension check form", clear_on_submit=True):
    st.subheader(
        "Based on the instructions above, once a sound is presented to you, what should you do?",
        anchor=False,
    )
    options = [
        ("Record myself imitating the sound", "distractor1"),
        (
            "Listen to the sound carefully and come up with a query to find similar sounds",
            "correct",
        ),
        ("Listen again without using headphones", "distractor2"),
        ("Sound libraries do not let you search for sounds using text", "distractor3"),
    ]
    for option, label in options:
        st.checkbox(option, key=label)
    submitted = st.form_submit_button("Submit", type="primary")

if submitted:
    correct = st.session_state["correct"]
    distractor1 = st.session_state["distractor1"]
    distractor2 = st.session_state["distractor2"]
    distractor3 = st.session_state["distractor3"]
    if correct and not (distractor1 or distractor2 or distractor3):
        st.success("Correct!")
        st.switch_page("pages/dispatch.py")
    else:
        error_text = """Incorrect! 
        Please carefully read the instructions and the question again.
        Only select answers that are relevant to the question."""
        st.error(error_text)
