import streamlit as st

from components.chat_interface import render_chat_interface
from components.sidebar import render_sidebar
from services.session_manager import initialize_session


# Configuración de la página
st.set_page_config(
    page_title="Asistente AI - Sistemas Inteligentes",
    page_icon="🤖",
    layout="centered",
)

# Encabezado
st.title("🤖 Asistente Virtual 'Astra'")

st.caption(
    "UAdeO • Materia: Sistemas Inteligentes • "
    "Dra. Aiblis Susej Herrera Palafox"
)

# Obtener credenciales
try:
    api_key = st.secrets["GEMINI_API_KEY"]

except Exception:
    st.error(
        "No se encontró GEMINI_API_KEY. "
        "Configura la clave en .streamlit/secrets.toml."
    )
    st.stop()

if not isinstance(api_key, str) or not api_key.strip():
    st.error("La API Key de Gemini no es válida.")
    st.stop()

# Inicializar conversación
initialize_session(api_key)

# Renderizar componentes
render_sidebar()
render_chat_interface()
