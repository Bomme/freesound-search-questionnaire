import streamlit as st


def toggle_session_state(key: str, condition_key=None) -> None:
    """
    Toggles the value of a boolean session state variable.

    :param key: The key of the variable in the streamlit session state.
    :param condition_key: An additional condition that is checked in the session state. If the condition is not met, the variable is not toggled.
    By default, the variable is toggled.
    """
    if condition_key is not None and not st.session_state.get(condition_key):
        return
    if key not in st.session_state:
        st.session_state[key] = True
    else:
        st.session_state[key] = not st.session_state[key]


def set_page_config():
    st.set_page_config(
        page_title="Sound Search Questionnaire",
        page_icon=":question:",
        initial_sidebar_state="collapsed",
    )


def redirect_if_no_session_state():
    if "user_id" not in st.session_state:
        if "user_id" in st.query_params:
            st.session_state["user_id"] = st.query_params["user_id"]
        st.switch_page("welcome.py")


def page_setup():
    """Common setup logic for all subpages. Must be called at the beginning of each page."""
    set_page_config()
    redirect_if_no_session_state()
    st.query_params["user_id"] = st.session_state["user_id"]
