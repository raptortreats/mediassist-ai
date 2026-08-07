from app.services.embedding_service import generate_query_embedding
from app.services.vector_store import search

def search_document(query: str):
    """
    search similar document chunks.
    """
    query_embedding = generate_query_embedding(query)

    results = search(query_embedding)

    return results