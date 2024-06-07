import streamlit as st

from backend.data_loading import get_single_description
from pages.shared_survey import aspects_form
from pages.utils import page_setup, toggle_session_state

page_setup()

st.subheader(
    "How would you search for a sound that matches this description?", anchor=False
)

if "stimulus_id" not in st.session_state:
    filename, description = get_single_description()
    st.session_state["stimulus"] = description
    st.session_state["stimulus_id"] = filename

with st.container(border=True):
    st.markdown(f"*{st.session_state['stimulus']}*")

st.divider()
st.subheader(
    "Imagine you are looking for a sound that matches above description. "
    "What would you type into the search bar?",
    anchor=False,
)

query_submitted = st.session_state.get("query1_submitted", False)

with st.form("query_form", border=False):
    query = st.text_input(
        "Search bar",
        help="Please type your query here",
        disabled=query_submitted,
        key="query1",
    )
    query = query.strip()

    st.form_submit_button(
        "Submit",
        on_click=toggle_session_state,
        args=["query1_submitted", "query1"],
        disabled=query_submitted,
        type="primary",
    )
    skipped = st.form_submit_button(
        "Skip and get a new description", disabled=query_submitted
    )


if skipped:
    del st.session_state["stimulus_id"]
    st.rerun()

if query and query_submitted:
    st.info(f"Your query:\n\n*{query}*")
    st.session_state["original_query"] = query

    followup_submitted = aspects_form()

    if followup_submitted:
        st.switch_page("pages/text_prompt_refine.py")
