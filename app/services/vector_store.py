import chromaDB

import uuid

client = chromaDB.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="medical_documents"
)

def add_documents(
        chunks: list[str],
        embeddings
):
    """
    Store chunks and embeddings
    """

    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )



def search(query_embedding, n_results=3):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
        )

    return results