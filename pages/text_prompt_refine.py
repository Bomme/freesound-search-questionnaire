import streamlit as st

from backend.data_loading import get_related_sound_for_description
from pages.shared_survey import query_comparison_form
from pages.utils import page_setup

page_setup()
num_items_completed = st.session_state['num_items_completed']
st.title(f"Set {num_items_completed // 3 + 1}: Example {num_items_completed % 3 + 1}", anchor=False)
if "sound_url2" not in st.session_state:
    sound_url, sound_id, start, end, license_str = get_related_sound_for_description(
        st.session_state["stimulus_id"]
    )
    st.session_state["sound_url2"] = sound_url
    st.session_state["audio_result_id"] = sound_id
    st.session_state["start"] = start
    st.session_state["end"] = end
    st.session_state["license_2"] = license_str

st.subheader("1️⃣This is the description of a sound you are looking for.", anchor=False)
st.info(
    "This describes a sound that you ***do*** want to be among the results. This is the description you viewed in the previous step.",
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
if st.session_state["license_2"]:
    st.caption(st.session_state["license_2"])

st.divider()

rewrite_instructions = "What would you type into the search bar to find sounds like the reference description 1️⃣ and avoid sounds like 2️⃣?"

query_comparison_form(rewrite_instructions)
