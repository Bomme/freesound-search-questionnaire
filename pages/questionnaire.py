import streamlit as st


if "user_id" not in st.session_state:
    st.switch_page("welcome.py")

options = [
    "Strongly disagree",
    "Disagree",
    "Neither agree nor disagree",
    "Agree",
    "Strongly agree",
]

st.title("Freesound search questionnaire", anchor=False)

st.header("User questionnaire", anchor=False)

with st.form("questionnaire_form"):
    st.write("Please answer the following questions about yourself.")
    st.subheader("How much do you agree with the following statements?", anchor=False)
    familiarity_fs = st.radio("I am familiar with Freesound", options=options, index=None, horizontal=True)
    familiarity_se = st.radio("I am familiar with sound effects", options=options, index=None)
    familiarity_sl = st.radio("I am familiar with sound libraries", options=options, index=None)
    familiarity_sd = st.radio("I am familiar with sound design", options=options, index=None)
    comfortable_en = st.radio("I am comfortable searching for sounds in the English language", options=options, index=None)
    submitted = st.form_submit_button(label="Submit", type="primary")

if submitted:
    if any([val is None for val in [familiarity_fs, familiarity_se, familiarity_sl, familiarity_sd, comfortable_en]]):
        st.warning("Please answer all questions.")
        # print(familiarity_fs, familiarity_se, familiarity_sl, familiarity_sd, comfortable_en)
    else:
        st.switch_page("pages/query_questionnaire.py")
