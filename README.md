# RAG Chatbot with Flask

This project implements a Retrieval-Augmented Generation (RAG) chatbot using LangChain, ChromaDB, and the Ollama LLM model.  
The chatbot is accessible via a simple web interface built with Flask.

---

## Features

- Semantic search in a PDF document database using ChromaDB.  
- Contextual response generation with an LLM model (Ollama - Mistral).  
- Simple web interface to ask questions and display answers.  
- Intelligent handling of specific questions (e.g., "Who are you?") with custom responses.  
- Suppresses TensorFlow warnings from output.  
- Easy deployment with Docker.

---

## Project Structure

/project
│
├── app.py # Main Flask application
├── chatbot.py # Chatbot RAG logic module
├── get_embedding_function.py # Embedding extraction function
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # HTML template for web UI

<pre><code>```plaintext /project │ ├── app.py # Main Flask application ├── chatbot.py # Chatbot RAG logic module ├── get_embedding_function.py# Embedding extraction function ├── requirements.txt # Python dependencies ├── templates/ │ └── index.html # HTML template for web UI ``` </code></pre>

---

## Installation

### Prerequisites

- Python 3.8+  
- Access to the Ollama model (configured and running)  
- Docker (optional, for containerized deployment)

---

### Clone the repository

```bash
git clone https://github.com/FayssalSabri/RAG-V2.git
cd RAG-V2


