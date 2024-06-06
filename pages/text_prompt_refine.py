import streamlit as st

from backend.data_loading import get_related_sound_for_description
from pages.shared_survey import aspects_form
from pages.utils import assert_user_id, toggle_session_state

assert_user_id()
st.title("Refine your query", anchor=False)

if "sound_url2" not in st.session_state:
    sound_url, sound_id, start, end = get_related_sound_for_description(
        st.session_state["stimulus_id"]
    )
    st.session_state["sound_url2"] = sound_url
    st.session_state["audio_result_id"] = sound_id
    st.session_state["start"] = start
    st.session_state["end"] = end

# st.write(f"{related_sound_url=} {start=} {end=}")
st.subheader("1️⃣This is the description of a sound you are looking for.", anchor=False)
st.info(
    "This description is an example of a sound that you ***do*** want to be among the results. This is the description you "
    "viewed in the previous step.",
    icon="✅",
)

with st.container(border=True):
    st.markdown(f"*{st.session_state['stimulus']}*")

st.subheader(
    "2️⃣Now imagine that the following sound was among the top results, but you do not want it.",
    anchor=False,
)
st.info(
    "Consider this sound as an example of a sound that you ***do not*** want to be among the results.",
    icon="❌",
)
st.audio(
    st.session_state["sound_url2"],
    format="audio/mp3",
    start_time=st.session_state["start"],
    end_time=st.session_state["end"],
)

st.divider()

query_submitted = st.session_state.get("query2_submitted", False)
with st.form("query_comparison_form", border=False):
    st.subheader(
        "What would you type into the search bar to find sounds like the reference description 1️⃣ and avoid sounds like 2️⃣?",
        anchor=False,
    )
    st.info(f"Your original query was:\n\n*{st.session_state.get('original_query')}*")
    query = st.text_input(
        "Search bar",
        disabled=query_submitted,
        key="query2",
    )
    query = query.strip()

    st.form_submit_button(
        label="Submit",
        type="primary",
        on_click=toggle_session_state,
        args=["query2_submitted", "query2"],
        disabled=query_submitted,
    )
    st.form_submit_button(
        label="I don't want to change my query",
        type="secondary",
        on_click=toggle_session_state,
        args=["query2_skipped"],
        disabled=query_submitted,
    )

if query and query_submitted:
    st.info(f"Your new query:\n\n*{query}*")

    st.session_state["refined_query"] = query
    followup_submitted = aspects_form(refine=True)

    if followup_submitted:
        st.switch_page("pages/dispatch.py")

if st.session_state.get("query2_skipped"):
    st.switch_page("pages/dispatch.py")
