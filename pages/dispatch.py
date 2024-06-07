from random import choice

import streamlit as st

from backend.database import add_annotation, num_annotations_for_participant
from pages.utils import page_setup

page_setup()


def store_results_and_clear_session_state():
    if "query1_submitted" not in st.session_state:
        return
    aspects = st.session_state.get("aspects")
    if "query_refined" not in st.session_state:
        aspects_refined = {}
    else:
        aspects_refined = st.session_state.get("aspects_refine")
    if st.session_state.get("query2_skipped"):
        st.session_state["refined_query"] = """<<SKIPPED>>"""
    add_annotation(
        st.session_state.get("user_id"),
        st.session_state.get("stimulus_id"),
        st.session_state["next_task"],
        st.session_state.get("audio_result_id"),
        st.session_state.get("original_query"),
        st.session_state.get("refined_query"),
        [key for key, val in aspects.items() if val],
        [key for key, val in aspects_refined.items() if val],
    )
    for key in [
        "original_query",
        "aspects",
        "aspects_refine",
        "query1_submitted",
        "query2_submitted",
        "query2_skipped",
        "query1",
        "query2",
        "sound_url",
        "refined_query",
        "description_id",
        "stimulus",
        "stimulus_id",
        "sound_url1",
        "sound_url2",
        "audio_result_id",
        "sound_class",
    ]:
        if key in st.session_state:
            del st.session_state[key]
    # if "counter_incremented" not in st.session_state:

    # st.session_state["counter_incremented"] = True


def set_next_task():
    tasks = ["audio", "image", "text"]
    next_task = choice(tasks)
    st.session_state["next_task"] = next_task


store_results_and_clear_session_state()
st.session_state["num_items_completed"] = num_annotations_for_participant(
    st.session_state["user_id"]
)
set_next_task()
if st.session_state["num_items_completed"] == 0:
    st.switch_page(f"pages/{st.session_state['next_task']}_prompt.py")
else:
    items = "items" if st.session_state["num_items_completed"] != 1 else "item"
    st.write(
        f"You have completed {st.session_state['num_items_completed']} {items}! Do you want to continue?"
    )
    st.page_link(
        f"pages/{st.session_state['next_task']}_prompt.py",
        label="Continue",
        icon="⏭",
        use_container_width=True,
    )
    st.page_link(
        "pages/open_question.py", label="End survey", icon="🔚", use_container_width=True
    )
    with st.expander("Debug", expanded=False):
        st.write(st.session_state)
