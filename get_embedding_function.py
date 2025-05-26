from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def get_embedding_function():

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
