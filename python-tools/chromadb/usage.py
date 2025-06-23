from chromadb import Client

chroma_client = Client()  # data does not store anywhere, just keep in RAM.

collection = chroma_client.get_or_create_collection(name="adnan_data")

# document: collection of sentence

docs = [
    "My name is Adnan",
    "I'm currently a BCA final year student.",
    "I'do love computer science.",
    "My passion is about AI and ML.",
]

# dummy embeddings
embds = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]

# collection operations
# create: .add()

collection.add(ids=["1", "2", "3", "4"], documents=docs, embeddings=embds)

# read: .query()
# parms:
#   - `query_embeddings`: the embeddings of the query text.
#   - `n_result` : top results.

q = "what is your name?"
q_embds = [8, 1, 3, 4, 2]
result = collection.query(query_embeddings=q_embds, n_results=2)

print(f"{result=}")


# delete: .delete()
# - we can delete either with `ids` or `where` clause
#
collection.delete(ids=["1"])

# update: .update()
# update with ids
collection.update(
    ids=["2"],
    documents=["my primary language is python. and i love that."],
    embeddings=[5, 1, 4, 3, 2],
)

# get: .get()
# get all documents

all_docs = collection.get(include=["documents", "metadatas"])
print(f"{all_docs=}")
