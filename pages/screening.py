import streamlit as st

from backend.database import add_participant
from pages.utils import assert_user_id

assert_user_id()
st.title("Sound search questionnaire", anchor=False)

st.header("Screening questions", anchor=False)

st.radio(
    "What is your English language proficiency?",
    options=["Native speaker", "Fluent", "Intermediate", "Basic", "Rather not say"],
    index=None,
    help="Please select the option that best describes your level in both speaking and writing.",
    key="fluency",
)

st.radio(
    "Have you used online sound libraries before?",
    options=["Yes", "No", "Rather not say"],
    index=None,
    help="Sound libraries are websites where you can search for and download sounds.",
    key="experience",
)
can_advance = all(st.session_state[key] for key in ["fluency", "experience"])
next_page = st.button("Continue", type="primary", disabled=not can_advance)
if next_page:
    add_participant(
        st.session_state["user_id"],
        st.session_state["fluency"],
        st.session_state["experience"],
    )
    st.switch_page("pages/instructions.py")
