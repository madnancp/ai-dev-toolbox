from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models.llamacpp import ChatLlamaCpp

llm = ChatLlamaCpp(
    model_path="../model/tinyllama-1.1b-chat-v1.0.Q6_K.gguf",
    streaming=True,
    verbose=False,
    n_threads=3,
    temperature=0.9,
    top_p=0.99,
    top_k=50,
)

prompt = ChatPromptTemplate.from_messages(
    messages=[
        (
            "system",
            "You are a playful assistant. When asked any question, you ONLY reply with 3–5 emojis that express the meaning. DO NOT use any words.",
        ),
        ("user", "{prompt}"),
    ]
)

chain = prompt | llm

for token in chain.stream({"prompt": "is javascript better than python?"}):
    print(token.content, flush=True, end="")
