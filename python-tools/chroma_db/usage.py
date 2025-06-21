from chromadb import Client
from chromadb.config import Settings


chroma_client = Client(Settings())
collection = chroma_client.get_or_create_collection(name="my_store")

docs = ["python is an awsome programming language.", "postgres is very good enough."]

embds = [[1, 2, 3, 4], [5, 6, 7, 8]]

collection.add(ids=["python", "psql"], documents=docs, embeddings=embds)
