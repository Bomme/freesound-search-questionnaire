"""This file contains the instructions for the experiment."""

import streamlit as st

from backend.database import participant_passed_instructions
from pages.utils import page_setup

page_setup()

st.title("Sound search questionnaire", anchor=False)

st.header("Instructions", anchor=False)


st.markdown(
    """
    🔎 In this experiment, you will be asked to search for sounds in a hypothetical sound library.
    
    🔠 You will only be able to use text to search for sounds. You will not be able to use any other search filters.
    
    🧠 Imagine a limitless system where you can find any sound in any way you can think of, using text only.
    
    📋 To guide your search, you will be given an example. The example will be either text, image or sound.
    
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

with st.form("Comprehension check form", clear_on_submit=True):
    st.subheader(
        "Based on the instructions above, once a sound is presented to you, what should you do?",
        anchor=False,
    )
    options = [
        ("Record myself imitating the sound", "distractor1"),
        (
            "Take inspiration from the example to come up with a search query for a hypothetical sound library",
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
        participant_passed_instructions(st.session_state["user_id"])
        st.switch_page("pages/dispatch.py")
    else:
        error_text = """Incorrect! 
        Please carefully read the instructions and the question again.
        Only select answers that are relevant to the question."""
        st.error(error_text)
