from services.embedding_service import generate_embeddings

texts = [
    "Artificial Intelligence in healthcare",
    "Drug discovery using machine learning"
]

embeddings = generate_embeddings(texts)

print(f"Generated {len(embeddings)} embeddings")
print(f"Embedding dimension: {len(embeddings[0])}")