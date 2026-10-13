import streamlit as st

from services.gemini_service import send_message
from services.session_manager import save_message


def render_chat_interface() -> None:
    """Renderiza y administra la interfaz conversacional."""

    # Mostrar historial de mensajes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada del usuario
    user_input = st.chat_input(
        "Escribe tu pregunta o duda aquí..."
    )

    if not user_input:
        return

    # Guardar y mostrar pregunta
    save_message("user", user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    # Consultar Gemini
    with st.chat_message("assistant"):
        with st.spinner("Pensando respuesta..."):
            try:
                response = send_message(
                    st.session_state.chat_session,
                    user_input,
                )

                st.markdown(response)
                save_message("assistant", response)

            except Exception as error:
                st.error(
                    f"Error al consultar la API: {error}"
                )
                