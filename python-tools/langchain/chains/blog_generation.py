from langchain_community.chat_models.llamacpp import ChatLlamaCpp
from langchain.schema.runnable import RunnableLambda
from langchain.prompts import ChatPromptTemplate

llm = ChatLlamaCpp(
    model_path="../model/tinyllama-1.1b-chat-v1.0.Q6_K.gguf",
    streaming=True,
    verbose=False,
    n_threads=3,
    temperature=0.7,
    top_p=0.99,
    top_k=50,
)


blog_title_prompt = ChatPromptTemplate.from_messages(
    messages=[
        ("system", "generate a short elegant blog title for {topic}"),
    ]
)

blog_outline_prompt = ChatPromptTemplate.from_messages(
    messages=[
        ("system", "generate an clear outline blog for {title} titled."),
    ]
)

title_extractor = RunnableLambda(lambda x: {"title": x.content})


chain = blog_title_prompt | llm | title_extractor | blog_outline_prompt | llm

for token in chain.stream({"topic": "critics"}):
    print(token.content, flush=True, end="")
