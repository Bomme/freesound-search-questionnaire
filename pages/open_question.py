import streamlit as st

from pages.utils import assert_user_id

assert_user_id()
st.title("Sound search questionnaire", anchor=False)

st.header("Comments", anchor=False)

with st.form("comments_form"):
    st.subheader("Do you have any comments or suggestions for us?", anchor=False)
    st.caption("(Optional)")
    st.text_area("Comments", height=100, label_visibility="collapsed")
    # How do you imagine searching for sounds in the future?
    st.subheader("How do you imagine searching for sounds in the future?", anchor=False)
    st.caption("(Optional)")
    st.text_area("Future", height=100, label_visibility="collapsed")
    submitted = st.form_submit_button(label="Submit", type="primary")

if submitted:
    st.switch_page("pages/end_of_survey.py")
