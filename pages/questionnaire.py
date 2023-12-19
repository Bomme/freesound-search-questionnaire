import streamlit as st
from streamlit_extras.switch_page_button import switch_page

if "user_id" not in st.session_state:
    switch_page("welcome")

options = [
    "Strongly disagree",
    "Disagree",
    "Neither agree nor disagree",
    "Agree",
    "Strongly agree",
]

st.title("Freesound search questionnaire", anchor=False)

st.header("User questionnaire", anchor=False)

with st.form("questionnaire_form", ):
    st.write("Please answer the following questions about yourself.")
    st.subheader("How much do you agree with the following statements?")

    st.radio("I am familiar with Freesound", options=options, index=None, horizontal=True)
    st.radio("I am familiar with sound effects", options=options, index=None)
    st.radio("I am familiar with sound libraries", options=options, index=None)
    st.radio("I am familiar with sound design", options=options, index=None)
    st.radio("I am comfortable searching for sounds in the English language", options=options, index=None)
    st.radio("I explore Freesound by browsing", options=options, index=None)
    st.radio("I explore Freesound by searching", options=options, index=None)
    submitted = st.form_submit_button(label="Submit", type="primary")

# st.button("Next", on_click=switch_page, args=["query_questionnaire"])
if submitted:
    switch_page("query_questionnaire")
