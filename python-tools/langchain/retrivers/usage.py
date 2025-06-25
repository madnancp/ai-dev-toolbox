# we here just explore most common or must known retriver classes and their use cases.

# setup an vector store.
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from chromadb import PersistentClient

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

client = PersistentClient()
collection = client.get_or_create_collection("my_test_2")
docs = [
    "Artificial Intelligence is fastly evolving.",
    "Python is the widely used language in AI/ML",
    "Golang is best for Backend.",
]
collection.add(ids=["001", "002", "003"], documents=docs)


vstore = Chroma(
    client=client, collection_name="my_test_2", embedding_function=embedding
)

# setup llm
from langchain_community.chat_models.llamacpp import ChatLlamaCpp

llm = ChatLlamaCpp(
    model_path="../model/tinyllama-1.1b-chat-v1.0.Q6_K.gguf", verbose=False
)

# 1. VectorStoreRetriever : most common
# `this just retrive document that have high score in semantic search.`
# params:
#   search_type     : which method search want to perform
#   search_kwargs   : vector_db search params, such as top_result, so on...

print("<< START OF `VectorStoreRetriever` >>")

retriver = vstore.as_retriever(search_kwargs={"k": 1})

result = retriver.invoke(input="what you know about AI?")
print(f"result : {result}")

print("<< END OF `VectorStoreRetriever` >>")


# 2. MultiQueryRetriever
# this require `llm` for functioning
# this modify user query into more better way, eg. `tell me about biriyani` => `what is biriyani`
# this will create 3 (by default) new query with user query that more meaning full and pass the 3 query into vector store and combine the result docs and return
from langchain.retrievers import MultiQueryRetriever

print("<< START OF `MultiQueryRetriever` >>")

retriver = MultiQueryRetriever.from_llm(
    llm=llm, retriever=vstore.as_retriever(search_kwargs={"k": 1})
)
result = retriver.invoke(input="what is python")
print(f"result: {result}")

print("<< END OF `MultiQueryRetriever` >>")
