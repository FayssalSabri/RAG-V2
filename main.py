import chainlit as cl
from chatbot import query_rag

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    response = query_rag(user_input)
    await cl.Message(content=response).send()
