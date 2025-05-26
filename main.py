# chatbot_chainlit.py

import os
import warnings

import chainlit as cl
from langchain_community.vectorstores import Chroma
from langchain_community.llms.ollama import Ollama
from langchain.prompts import ChatPromptTemplate

from get_embedding_function import get_embedding_function

warnings.filterwarnings("ignore")

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are a helpful and friendly AI assistant created by Fayssal. 
If someone asks who you are (e.g., "Who are you?", "Qui es-tu ?", "C’est quoi ce chatbot ?"),
you should answer: "I'm an AI agent created by Fayssal to help you. Feel free to ask me any questions you may have about Monopoly." or in French: "Je suis un agent IA créé par Fayssal pour vous aider. N'hésitez pas à me poser toutes vos questions sur le jeu Monopoly.".
if someone asks who is Fayssal, you should answer: "Fayssal is an AI and data science engineer who developed this AI assistant to answer your Monopoly-related questions."
Use the context below to answer the question if relevant. If the context is not helpful, use your own knowledge based on the instructions.

Context:
{context}

---

Question: {question}
Answer:
"""

# Chargement au démarrage de la session
@cl.on_chat_start
async def setup():
    # Charger la base vectorielle et le modèle une seule fois
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    model = Ollama(model="mistral")

    cl.user_session.set("db", db)
    cl.user_session.set("model", model)

    await cl.Message(content="👋 Hi! Ask me a question about the Monopoly game.").send()


# Lorsqu'un message est reçu
@cl.on_message
async def handle_message(message: cl.Message):
    db = cl.user_session.get("db")
    model = cl.user_session.get("model")
    query = message.content

    # Rechercher les passages pertinents
    results = db.similarity_search_with_score(query, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])

    # Construire le prompt
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)

    # Générer la réponse
    response_text = model.invoke(prompt)

    await cl.Message(content=response_text).send()
