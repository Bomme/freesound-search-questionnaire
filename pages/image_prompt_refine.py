import streamlit as st

from pages.shared_survey import query_comparison_form
from pages.utils import page_setup

page_setup()
num_items_completed = st.session_state['num_items_completed']
st.title(f"Set {num_items_completed // 3 + 1}: Example {num_items_completed % 3 + 1}", anchor=False)
st.subheader(
    "1️⃣ This is the image that you want to find an accompanying sound for.",
    anchor=False,
)
st.info(
    "This shows a scene that you ***do*** want to find a sound for. This is the image you viewed in the previous step.",
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

query_comparison_form(rewrite_instructions)
