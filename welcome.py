import uuid

import streamlit as st

from backend.database import get_participant
from pages.utils import set_page_config

set_page_config()

query_params = st.query_params.to_dict()

if "user_id" in query_params and st.session_state.get("user_id"):
    # if we got redirected after a refresh, we need to re-add the query params
    st.query_params["user_id"] = st.session_state["user_id"]
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())

if (participant := get_participant(st.session_state["user_id"])) is not None:
    if participant.passed_instructions:
        st.switch_page("pages/dispatch.py")
    else:
        st.switch_page("pages/instructions.py")

st.title("Sound search questionnaire", anchor=False)


st.markdown(
    """This questionnaire is part of a research project conducted by the [MTG](https://www.upf.edu/web/mtg) at 
    [Universitat Pompeu Fabra](https://www.upf.edu) in Barcelona, Spain.
    The questionnaire is anonymous and the data collected will be used for research purposes only."""
)

intro = """
   ###

   🎵 You will be asked to perform imaginative tasks and answer questions about how you search for sounds.

   ✍️ By contributing to this questionnaire, you are helping us to understand how people would like to search for sounds
   in the future. This will enable us to develop better sound search tools. We really appreciate your help!

   ℹ️ We will only collect data you provide by submitting your answers. No other personal information will be collected.
   
   ⏱ The questionnaire will take approximately 12 - 15 minutes to complete.
   
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
