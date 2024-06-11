import streamlit as st

from backend.data_loading import get_sound_from_class
from pages.shared_survey import aspects_form, query_comparison_form
from pages.utils import page_setup

page_setup()
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
rewrite_instructions = "What would you type into the search bar to find sounds for the image 1️⃣ and avoid sounds like 2️⃣?"

query_submitted, query = query_comparison_form(rewrite_instructions)

if query and query_submitted:
    st.info(f"Your new query:\n\n*{query}*")

    st.session_state["refined_query"] = query
    st.session_state["result_relevance"] = st.session_state["result_relevance_score"]
    followup_submitted = aspects_form(refine=True)

    if followup_submitted:
        st.switch_page("pages/dispatch.py")

if st.session_state.get("query2_skipped"):
    st.switch_page("pages/dispatch.py")
