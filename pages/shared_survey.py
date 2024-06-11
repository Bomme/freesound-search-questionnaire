import random

import streamlit as st

from pages.utils import toggle_session_state


def gather_aspects(refine=False):
    if refine:
        key_suffix = "_refine"
    else:
        key_suffix = ""
    aspects = {}
    for key in [
        "temporal_order",
        "number_sources",
        "pitch",
        "color_density",
        "duration",
        "loudness",
        "rhythm",
        "main_source",
        "usage",
        "emotion",
        "quality",
        "location",
    ]:
        aspects[key] = st.session_state[f"{key}{key_suffix}"]

    aspects["additional_aspects"] = st.session_state[f"additional_aspects{key_suffix}"]
    st.session_state[f"aspects{key_suffix}"] = aspects


def aspects_form(refine=False):
    if refine:
        writing = "refining"
        key_suffix = "_refine"
    else:
        writing = "writing"
        key_suffix = ""
    st.subheader(
        f"What did you consider important for {writing} your query?", anchor=False
    )
    st.write("Please select all that apply.")
    st.caption(
        "You can hover or click the question mark icon on each option for more information."
    )
    options = [
        (
            "The **temporal order** of events in the sound",
            "The order in which events occur in time, e.g. first/last, before/after, simultaneously",
            f"temporal_order{key_suffix}",
        ),
        (
            "The **number** of sound sources",
            "How many sound sources there are",
            f"number_sources{key_suffix}",
        ),
        (
            "The **pitch** of the sound",
            "The perceived frequency of the sound, e.g. high/low",
            f"pitch{key_suffix}",
        ),
        (
            "The **color** and/or **density** of the sound",
            "The perceived quality and/or composition of the sound, e.g. bright/dark, warm/cold, harsh/smooth and simple/complex, sparse/dense, clear/thick",
            f"color_density{key_suffix}",
        ),
        (
            "The **duration** of the sound",
            "How long the sound lasts, e.g. short/long",
            f"duration{key_suffix}",
        ),
        (
            "The **loudness** of the sound",
            "How loud or quiet the sound is",
            f"loudness{key_suffix}",
        ),
        (
            "The **rhythm** of the sound",
            "The perceived regularity or irregularity of the sound, e.g. repetitive/chaotic, fast/slow",
            f"rhythm{key_suffix}",
        ),
        (
            "The **main sound source**",
            "The most prominent and recognizable object, entity or event in the sound",
            f"main_source{key_suffix}",
        ),
        (
            "The **usage** context of the sound",
            "What the sound could be used for, e.g. in a movie, in a game, in a commercial",
            f"usage{key_suffix}",
        ),
        (
            "The **perceived emotion** of the sound",
            "How the sound makes you feel",
            f"emotion{key_suffix}",
        ),
        (
            "The **recording quality** of the sound",
            "The perceived fidelity of the sound, i.e. how clear or noisy it is",
            f"quality{key_suffix}",
        ),
        (
            "The **recording setting** of the sound",
            "The perceived space and environment in which the sound was recorded",
            f"location{key_suffix}",
        ),
    ]
    rng = random.Random(st.session_state.get("user_id"))
    rng.shuffle(options)
    with st.form("desc_form", clear_on_submit=True, border=False):
        for option, help_str, key in options:
            st.checkbox(option, help=help_str, key=key)
        st.text_input(
            "Please add any aspects that are important to you but not listed above.",
            key=f"additional_aspects{key_suffix}",
            placeholder="add your own",
        )

        followup_submitted = st.form_submit_button(
            "Submit", type="primary", on_click=gather_aspects, args=[refine]
        )
        return followup_submitted


def query_comparison_form(rewrite_instructions: str):
    query_submitted = st.session_state.get("query2_submitted", False)
    with st.form("query_comparison_form", border=False):
        st.radio(
            "How relevant is this sound to your query?",
            options=[0, 1, 2, 3, 4],
            format_func=[
                "Not relevant",
                "Slightly relevant",
                "Moderately relevant",
                "Strongly relevant",
                "Perfect match",
            ].__getitem__,
            index=None,
            key="result_relevance_score",
        )

        st.subheader(rewrite_instructions, anchor=False)
        st.info(
            f"Your original query was:\n\n*{st.session_state.get('original_query')}*"
        )
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
            args=["query2_submitted", "query2", "result_relevance_score"],
            disabled=query_submitted,
        )
        st.form_submit_button(
            label="I don't want to change my query",
            type="secondary",
            on_click=toggle_session_state,
            args=["query2_skipped", "result_relevance_score"],
            disabled=query_submitted,
        )

    if query and query_submitted:
        st.info(f"Your new query:\n\n*{query}*")

        st.session_state["refined_query"] = query
        st.session_state["result_relevance"] = st.session_state["result_relevance_score"]

        followup_submitted = aspects_form(refine=True)

        if followup_submitted:
            st.switch_page("pages/dispatch.py")

    if st.session_state.get("query2_skipped"):
        st.session_state["result_relevance"] = st.session_state["result_relevance_score"]
        st.switch_page("pages/dispatch.py")
