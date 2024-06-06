import uuid

import streamlit as st


if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())

st.set_page_config(
    page_title="Sound search questionnaire",
    page_icon=":question:",
    initial_sidebar_state="collapsed",
)

st.title("Sound search questionnaire", anchor=False)


st.markdown(
    """This questionnaire is part of a research project conducted by the [MTG](https://www.upf.edu/web/mtg) at 
    [Universitat Pompeu Fabra](https://www.upf.edu) in Barcelona, Spain.
    The questionnaire is anonymous and the data collected will be used for research purposes only."""
)

intro = """
   ###

   🎵 You will be asked to perform an imaginative tasks and answer questions about how you search for sounds.

   ✍️ By contributing to this questionnaire, you are helping us to understand how people would like to search for sounds
   in the future. This will enable us to develop better sound search tools. We really appreciate your help!

   ℹ️ We will only collect data you provide by submitting your answers and no other personal information.
   
   Please read the following Participant Information Sheet and Informed Consent Form carefully before proceeding.
   """

informed_consent = """
    I HEREBY CONFIRM that:
    * I have read the information sheet regarding the research project,
    * I have been able to formulate questions on the project,
    * I have received enough information on the project,
    * I fulfill the inclusion criteria, and I am above 14 years old.
    
    I UNDERSTAND that my participation is voluntary and that I can withdraw from or opt out
    of the study at any time without any need to justify my decision.
   """

with open("information_sheet.md", "r") as f:
    information_sheet = f.read()

st.write(intro)

with st.expander("Show/hide Participant Information Sheet", expanded=True):
    st.header("Participant Information Sheet", anchor=False)
    st.markdown(information_sheet)

st.header("Informed Consent Form", anchor=False)
st.markdown(informed_consent)

agreed = st.checkbox("I GIVE MY CONSENT to participate in this study.", value=False)
st.caption(
    "Please check the box to confirm that you agree with the statements above or close this page if you do not agree."
)
_, col3, _ = st.columns([2, 1, 2])

proceed = col3.button(
    "Get started",
    type="primary",
    disabled=not agreed,
    help="Check the box to confirm that you agree with the statements above.",
)
if agreed and proceed:
    st.switch_page("pages/screening.py")
