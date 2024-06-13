import os
import time
from random import choice

import streamlit as st

from backend.database import add_annotation, num_annotations_for_participant
from pages.utils import page_setup

page_setup()

DEBUG = os.environ.get("DEBUG")


def store_results_and_clear_session_state():
    if "query1_submitted" not in st.session_state:
        return
    now = time.monotonic()
    if "time" not in st.session_state:
        time_elapsed = None
    else:
        time_elapsed = now - st.session_state["time"]
    aspects = st.session_state.get("aspects")
    if "refined_query" not in st.session_state:
        aspects_refined = {}
    else:
        aspects_refined = st.session_state.get("aspects_refine")
    if st.session_state.get("query2_skipped"):
        st.session_state["refined_query"] = """<<SKIPPED>>"""
    aspects_items = [key for key, val in aspects.items() if val]
    if "additional_aspects" in aspects:
        aspects_items.append(aspects["additional_aspects"])
    refined_aspects_items = [key for key, val in aspects_refined.items() if val]
    if "additional_aspects" in aspects_refined:
        refined_aspects_items.append(aspects_refined["additional_aspects"])
    add_annotation(
        st.session_state.get("user_id"),
        st.session_state.get("stimulus_id"),
        st.session_state["next_task"],
        st.session_state.get("audio_result_id"),
        st.session_state.get("original_query"),
        st.session_state.get("refined_query"),
        aspects_items,
        refined_aspects_items,
        st.session_state.get("result_relevance", -1),
        time_elapsed,
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
        "result_relevance",
        "description_id",
        "stimulus",
        "stimulus_id",
        "sound_url1",
        "sound_url2",
        "audio_result_id",
        "sound_class",
        "time",
    ]:
        if key in st.session_state:
            del st.session_state[key]


def set_next_task():
    if "next_task" in st.session_state:
        next_task_map = {"audio": "image", "image": "text", "text": "audio"}
        next_task = next_task_map[st.session_state["next_task"]]
    else:
        tasks = ["audio", "image", "text"]
        next_task = choice(tasks)
    st.session_state["next_task"] = next_task


store_results_and_clear_session_state()
st.session_state["num_items_completed"] = num_annotations_for_participant(
    st.session_state["user_id"]
)
set_next_task()
num_sets = st.session_state["num_items_completed"] // 3
if num_sets >= 7:
    st.switch_page("pages/open_question.py")
elif (
    num_sets >= 3 and (st.session_state["num_items_completed"] % 3) == 0
):
    items = "sets" if num_sets != 1 else "set"
    st.write(
        f"You have completed {num_sets} {items}!\n\nWe recommend completing 3 - 7 sets. Do you want to continue?"
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
    if DEBUG:
        with st.expander("Debug", expanded=False):
            st.write(st.session_state)
else:
    st.switch_page(f"pages/{st.session_state['next_task']}_prompt.py")
