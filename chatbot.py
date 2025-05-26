from langchain_community.vectorstores import Chroma
from langchain_community.llms.ollama import Ollama
from langchain.prompts import ChatPromptTemplate
from get_embedding_function import get_embedding_function
import warnings
warnings.filterwarnings("ignore")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'  # Pour masquer les logs d'infos et warnings de TensorFlow

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


def query_rag(query_text: str):
    # Préparer la base vectorielle
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Recherche des documents les plus similaires
    results = db.similarity_search_with_score(query_text, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    
    # Création du prompt
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Génération de la réponse
    model = Ollama(model="mistral")  # ou autre modèle disponible chez toi
    response_text = model.invoke(prompt)

    return response_text

def main():
    print("🤖 Hi ! Ask me a question (or type 'exit' or 'quit' to quit).")
    while True:
        user_input = input("❓ Vous: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Au revoir !")
            break
        response = query_rag(user_input)
        print(f"🤖 Réponse: {response}\n")


if __name__ == "__main__":
    main()
