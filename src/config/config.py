import os
from crewai import OpenAI, QdrantMemory, ChromaDBMemory

def get_llm():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_memory():
    if os.getenv("QDRANT_API_KEY") and os.getenv("QDRANT_URL"):
        return QdrantMemory(
            api_key=os.getenv("QDRANT_API_KEY"),
            url=os.getenv("QDRANT_URL")
        )
    elif os.getenv("CHROMADB_URL"):
        return ChromaDBMemory(url=os.getenv("CHROMADB_URL"))
    return None