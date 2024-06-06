import streamlit as st

from backend.data_loading import get_sound_from_class
from pages.shared_survey import aspects_form
from pages.utils import assert_user_id, toggle_session_state

assert_user_id()
st.title("Refine your query", anchor=False)

if "sound_url2" not in st.session_state:
    sound_id, sound_url = get_sound_from_class(st.session_state["sound_class"])
    st.session_state["sound_url2"] = sound_url
    st.session_state["audio_result_id"] = sound_id

st.subheader(
    "1️⃣ This is the image that you want to find an accompanying sound for.",
    anchor=False,
)
st.info(
    "This image is an example of an image that you ***do*** want to find a matching sound for. This is the image you "
    "viewed in the previous step.",
    icon="✅",
)

st.image(st.session_state["stimulus"], use_column_width=True)

st.subheader(
    "2️⃣ Now imagine that the following sound was among the top results, but you do not want it.",
    anchor=False,
)
st.info(
    "Consider this sound as an example of a sound that you ***do not*** want to be among the results.",
    icon="❌",
)
st.audio(st.session_state["sound_url2"], format="audio/mp3")

st.divider()

query_submitted = st.session_state.get("query2_submitted", False)
with st.form("query_comparison_form", border=False):
    st.subheader(
        "What would you type into the search bar to find sounds for the image 1️⃣ and avoid sounds like 2️⃣?",
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
