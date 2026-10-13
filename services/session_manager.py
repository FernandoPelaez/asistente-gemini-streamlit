import streamlit as st

from services.gemini_service import create_chat, reset_chat


def get_initial_messages() -> list[dict[str, str]]:
    """Devuelve el saludo inicial del asistente."""

    return [
        {
            "role": "assistant",
            "content": (
                "¡Hola! Soy Astra. "
                "¿En qué tema de Sistemas Inteligentes "
                "te puedo ayudar hoy?"
            ),
        }
    ]


def initialize_session(api_key: str) -> None:
    """Inicializa el cliente y el historial."""

    needs_initialization = (
        "chat_session" not in st.session_state
        or st.session_state.get("current_api_key") != api_key
    )

    if needs_initialization:
        client, chat = create_chat(api_key)

        st.session_state.client = client
        st.session_state.chat_session = chat
        st.session_state.current_api_key = api_key
        st.session_state.messages = get_initial_messages()

    elif "messages" not in st.session_state:
        st.session_state.messages = get_initial_messages()


def reset_conversation() -> None:
    """Reinicia la conversación y su historial."""

    st.session_state.chat_session = reset_chat(
        st.session_state.client
    )

    st.session_state.messages = get_initial_messages()


def save_message(role: str, content: str) -> None:
    """Guarda un mensaje en el historial."""

    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )
    