from google import genai

from config import CONFIG_INSTRUCCIONES, MODEL_NAME


def create_chat(api_key: str):
    """Crea el cliente y una sesión de Gemini."""

    client = genai.Client(api_key=api_key)

    chat = client.chats.create(
        model=MODEL_NAME,
        config=CONFIG_INSTRUCCIONES,
    )

    return client, chat


def send_message(chat, message: str) -> str:
    """Envía un mensaje y devuelve la respuesta."""

    response = chat.send_message(message)

    if not response.text:
        raise ValueError(
            "Gemini no devolvió una respuesta."
        )

    return response.text


def reset_chat(client):
    """Crea una conversación nueva."""

    return client.chats.create(
        model=MODEL_NAME,
        config=CONFIG_INSTRUCCIONES,
    )
