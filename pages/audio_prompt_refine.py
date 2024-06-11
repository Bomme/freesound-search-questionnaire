import streamlit as st

from backend.data_loading import get_sounds_from_same_class
from pages.shared_survey import query_comparison_form
from pages.utils import page_setup

page_setup()
st.title("Refine your query", anchor=False)

if "audio_result_id" not in st.session_state:
    sound_1, sound_2 = get_sounds_from_same_class(st.session_state.get("stimulus_id"))
    st.session_state["audio_result_id"] = sound_2[1]
    st.session_state["sound_url2"] = sound_2[0]

st.subheader("1️⃣ This is the sound you are looking for.", anchor=False)
st.info(
    "This sound is an example of a sound that you ***do*** want to be among the results. This is the sound you "
    "listened to in the previous step.",
    icon="✅",
)

st.audio(st.session_state["sound_url1"], format="audio/mp3", start_time=0)

st.subheader(
    "2️⃣ Now imagine that the following sound was among the top results, but you do not want it.",
    anchor=False,
)
st.info(
    "Consider this sound as an example of a sound that you ***do not*** want to be among the results.",
    icon="❌",
)
st.audio(st.session_state["sound_url2"], format="audio/mp3", start_time=0)

st.divider()
rewrite_instructions = "What would you type into the search bar to find sounds like the reference sound 1️⃣ and avoid sounds like 2️⃣?"

query_comparison_form(rewrite_instructions)
