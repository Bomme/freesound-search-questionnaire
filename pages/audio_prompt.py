import streamlit as st

from backend.data_loading import get_sounds_from_same_class
from pages.shared_survey import aspects_form
from pages.utils import assert_user_id, toggle_session_state


assert_user_id()
st.title("Query for a sound", anchor=False)

st.subheader("How would you search for a sound like this?", anchor=False)

if "stimulus_id" not in st.session_state:
    (sound_url1, sound_id1), (sound_url2, sound_id2) = get_sounds_from_same_class()
    st.session_state["sound_url1"] = sound_url1
    st.session_state["stimulus_id"] = sound_id1
    st.session_state["sound_url2"] = sound_url2
    st.session_state["audio_result_id"] = sound_id2


st.audio(st.session_state["sound_url1"], format="audio/mp3", start_time=0)

st.subheader(
    "Imagine you are looking for a sound exactly like the one above. "
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
        "Skip and get a new sound", disabled=query_submitted
    )

if skipped:
    del st.session_state["stimulus_id"]
    st.rerun()


if query and query_submitted:
    st.info(f"Your query:\n\n*{query}*")

    st.session_state["original_query"] = query

    followup_submitted = aspects_form()
    if followup_submitted:
        st.switch_page("pages/audio_prompt_refine.py")
