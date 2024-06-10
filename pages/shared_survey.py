import random

import streamlit as st


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
        "spatial",
        "rhythm",
        "main_source",
        "usage",
        "emotion",
        "quality",
    ]:
        aspects[key] = st.session_state[f"{key}{key_suffix}"]

    aspects["additional_aspects"] = st.session_state[f"additional_aspects{key_suffix}"]
    st.session_state["aspects" + key_suffix] = aspects


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
            "The **spatial** characteristics of the sound",
            "How the sound is perceived to be located or moving in space, e.g. left/right, front/back, up/down, near/far",
            f"spatial{key_suffix}",
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
            "What the sound could be used for",
            f"usage{key_suffix}",
        ),  # examples?
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
    ]
    random.seed(st.session_state.get("user_id"))
    random.shuffle(options)
    with st.form("desc_form", clear_on_submit=True, border=False):
        for option, help_str, key in options:
            st.checkbox(option, help=help_str, key=key)
        st.text_input(
            "Please add any aspects that are important to you but not listed above.",
            key=f"additional_aspects{key_suffix}",
            placeholder="...",
        )

        followup_submitted = st.form_submit_button(
            "Submit", type="primary", on_click=gather_aspects, args=[refine]
        )
        return followup_submitted
