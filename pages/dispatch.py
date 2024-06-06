from random import random

import streamlit as st

from backend.database import add_annotation
from pages.utils import assert_user_id

assert_user_id()


def store_results_and_clear_session_state():
    if "query1_submitted" not in st.session_state:
        return
    aspects = st.session_state.get("aspects")
    if "query_refined" not in st.session_state:
        aspects_refined = {}
    else:
        aspects_refined = st.session_state.get("aspects_refine")
    # TODO: cover all stimuli types
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
    st.session_state["num_items_completed"] += 1
    # st.session_state["counter_incremented"] = True


def set_next_task():
    if rand_choice := random() < 0.33:
        next_task = "text"
    elif rand_choice < 0.66:
        next_task = "image"
    else:
        next_task = "audio"
    st.session_state["next_task"] = next_task


if "num_items_completed" not in st.session_state:
    set_next_task()
    st.session_state["num_items_completed"] = 0

    # if st.session_state["num_items_completed"] < 1:
    st.switch_page(f"pages/{st.session_state['next_task']}_prompt.py")
else:
    store_results_and_clear_session_state()
    set_next_task()
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
