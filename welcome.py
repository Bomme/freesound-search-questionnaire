import uuid

import streamlit as st


if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())

st.set_page_config(page_title="Freesound search questionnaire", page_icon=":question:",
                   initial_sidebar_state="collapsed")

st.title("Freesound search questionnaire", anchor=False)

st.markdown(
    """This questionnaire is part of a research project conducted by the [MTG](https://www.upf.edu/web/mtg) at 
    [Universitat Pompeu Fabra](https://www.upf.edu) in Barcelona, Spain.
    The goal of this project is to understand how people search for sounds in Freesound.
    The questionnaire is anonymous and the data collected will be used for research purposes only.
    If you have any questions, please contact [📧 Benno Weck](mailto:benno.weck01@estudiant.upf.edu)"""
)

intro = """
   ###

   🎵 You will be asked to listen to some sounds and write a description for it.

   ✍️ By contributing to this questionnaire, you are helping us to understand how people would like to search for sounds
   in the future and how we can improve Freesound. We really appreciate your help!

   ℹ️ We will only collect data you provide by submitting your answers and no other 
   personal information.
   """

informed_consent = """
   ___ 
   📋 This survey is part of a research project being undertaken by Universitat Pompeu Fabra (the “Research Team”).
   By participating in this survey, you acknowledge and agree to the following:

   * You must be aged 18 or over
   * You are participating in an academic study, the results of which may or may not be published in an academic journal. 
   * Your participation is voluntary and you are free to leave at any time.
   * All intellectual property rights which may arise or inure to you as a result of your participation in this survey are hereby assigned jointly, in full and in equal proportion to the members of the Research Team.
   * By participating in this study, you agree to waive any moral rights of authorship that you may have in the responses that you provide in the survey to the extent permitted by law.
   * The data collected by this survey is intended to be published and shall be freely available to all. The responses submitted by you shall not be attributable to you and your participation in the survey shall remain confidential.

   """

st.write(intro)

st.write(informed_consent)

_, col3, _ = st.columns([2, 1, 2])
# col3.link_button(
#     "Get started",
#     "http://localhost:8501/questionnaire",
#     help="By clicking here, you confirm that you agree with the statements above.",
#     type="primary",
# )

agreed = col3.button(
    "Get started",
    # on_click=partial(switch_page, "questionnaire"),
    help="By clicking here, you confirm that you agree with the statements above.",
    type="primary",
)
if agreed:
    st.switch_page("pages/questionnaire.py")
