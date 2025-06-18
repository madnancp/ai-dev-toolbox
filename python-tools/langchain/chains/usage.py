from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models.llamacpp import ChatLlamaCpp

prompt = ChatPromptTemplate.from_messages(
    messages=[
        (
            "system",
            "your are a comedian. with have a good humar sence. and keep the joke very short",
        ),
        ("user", "Say comedy {count} comedy about {topic}."),
    ]
)
llm = ChatLlamaCpp(
    model_path="../model/tinyllama-1.1b-chat-v1.0.Q6_K.gguf",
    streaming=True,
    verbose=False,
    n_threads=3,
)

chain = prompt | llm

for token in chain.stream({"count": 2, "topic": "Programming"}):
    print(token.content, flush=True, end="")
