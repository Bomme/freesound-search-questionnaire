import streamlit as st

from backend.database import add_comments
from pages.utils import page_setup

page_setup()
st.title("Sound search questionnaire", anchor=False)

st.header("Comments", anchor=False)

with st.form("comments_form"):
    st.subheader("Do you have any comments or suggestions for us?", anchor=False)
    st.caption("(Optional)")
    comment_general = st.text_area("Comments", height=100, label_visibility="collapsed")
    st.subheader("How do you imagine searching for sounds in the future?", anchor=False)
    st.caption("(Optional)")
    comment_future = st.text_area("Future", height=100, label_visibility="collapsed")
    submitted = st.form_submit_button(label="Submit", type="primary")
    skipped = st.form_submit_button(label="Skip", type="secondary")

if submitted:
    add_comments(
        st.session_state["user_id"],
        comment_general,
        comment_future,
    )
    st.switch_page("pages/end_of_survey.py")

if skipped:
    st.switch_page("pages/end_of_survey.py")
