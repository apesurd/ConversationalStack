import streamlit as st
from core.util import get_response as get_ai_response

st.title("Conversational Stack")


# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def update_chat_history(role: str, message: str):
    st.session_state.chat_history.append({"role": role, "content": message})


# display chat messages from history on app reload
for this_message in st.session_state.chat_history:
    with st.chat_message(this_message["role"]):
        st.markdown(this_message["content"])


# react to user input
if prompt := st.chat_input("Say something"):
    with st.chat_message("user"):
        st.markdown(prompt)
    update_chat_history("user", prompt)

    response = get_ai_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    update_chat_history("assistant", response)
