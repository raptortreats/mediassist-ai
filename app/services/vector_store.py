import chromadb

import uuid

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="medical_documents"
)

def add_documents(
        chunks: list[str],
        embeddings,
        document_id: str,
        original_filename: str
):
    """
    Store chunks and embeddings
    """

    ids = [str(uuid.uuid4()) for _ in chunks]

    metadatas = [
        {
            "document_id": document_id,
            "original_filename": original_filename
        }
        for _ in chunks
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas = metadatas
    )

    print(collection.count())



def search(query_embedding, document_id: str, n_results=3):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results,
        where={"document_id": document_id}
        )

    return results

def get_documents():
    results = collection.get(
        include=["metadatas"]
    )

    print(results["metadatas"])

    documents = {}

    for metadata in results["metadatas"]:
        if not metadata:
            continue

        document_id = metadata.get("document_id")
        original_filename = metadata.get("original_filename")

        if not document_id or not original_filename:
            continue

        documents[document_id] = original_filename

    return [
        {
            "document_id": document_id,
            "original_filename": original_filename
        }
        for document_id, original_filename in documents.items()
    ]