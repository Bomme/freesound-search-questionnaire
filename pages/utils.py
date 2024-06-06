import streamlit as st


def assert_user_id():
    if "user_id" not in st.session_state:
        st.switch_page("welcome.py")
    with st.sidebar:
        st.write(st.session_state)


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
