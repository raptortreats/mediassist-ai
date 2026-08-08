from app.services.embedding_service import generate_query_embedding
from app.services.vector_store import search
#from app.services.embedding_service import generate_query_embedding
from app.services.vector_store import search
from app.services.llm_service import answer_question


def search_document(query: str):

    query_embedding = generate_query_embedding(query)

    results = search(query_embedding)

    context = "\n\n".join(results["documents"][0])

    answer = answer_question(query, context)

    return {
        "answer": answer,
        "context": results["documents"][0]
    }