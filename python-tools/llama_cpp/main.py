# example of load model from HG hub.
# return output as Streaming.

from llama_cpp import Llama


# load model from HF hub.
model_name: str = "TheBloke/Llama-2-7B-Chat-GGUF"
file_name: str = "llama-2-7b-chat.Q2_K.gguf"
model = Llama.from_pretrained(
    repo_id=model_name, filename=file_name, verbose=False, stream=True
)


res = model.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "you are a helpfull ai assistant who replay answer to user query, and answer them question with very short matured answer with some fun and kindness. just ask them about if they doing well.",
        },
        {
            "role": "user",
            "content": "what is Biryani?, have you heard about it?",
        },
    ],
    temperature=0.4,
    top_k=40,
    top_p=0.9,
    stream=True,
)

for token in res:
    print(token["choices"][0]["delta"].get("content", ""), end="", flush=True)


# result:-
# Hey there! *adjusts glasses* Oh, you want to know about Biryani? Well, let me tell you, it's a delicious and flavorful dish that originated in the Indian subcontinent! *winks* It's a mixture of basmati rice, spices, and meat (or vegetables) that's cooked to perfection. *nods*
# Haven't heard of it? *giggles* Well, you're in for a treat! Biryani is a popular dish in many parts of the world, especially in India, Pakistan, and Bangladesh. It's a staple dish in many South Asian cultures and is often served on special occasions like weddings and festivals. *smiles*
# So , what do you think? Are you ready to try some Biryani? *winks*%
