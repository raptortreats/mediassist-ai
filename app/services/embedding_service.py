from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks: list[str]):
    """
    Generate embeddings for text chunks.
    """
    embeddings = model.encode(chunks)

    return embeddings

def generate_query_embedding(query: str):
    """
    Generate an embedding for a user's question
    """

    return model.encode(query)

