from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embedding_function():
    # embeddings = OllamaEmbeddings(
    #     model="nomic-embed-text"
    # )
    embeddings = HuggingFaceEmbeddings()
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
