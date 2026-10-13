import streamlit as st

from config import MODEL_NAME
from services.session_manager import reset_conversation


def render_sidebar() -> None:
    """Muestra los controles de la aplicación."""

    with st.sidebar:
        st.header("⚙️ Opciones del Agente")

        st.markdown(
            f"Modelo backend: **{MODEL_NAME}**"
        )

        if st.button(
            "🧹 Limpiar conversación",
            use_container_width=True,
        ):
            reset_conversation()
            st.rerun()
            