from llama_cpp import Llama


class LLMInference:
    def __init__(
        self,
        hf_repo_name: str = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
        hf_filename: str = "tinyllama-1.1b-chat-v1.0.Q8_0.gguf",
    ) -> None:
        print("model loading from HF hub, please wait ....")

        self.model = Llama.from_pretrained(
            repo_id=hf_repo_name,
            filename=hf_filename,
            verbose=False,
            n_threads=4,
            stream=True,
        )
        print("model loading completed!")

    def get_output(
        self,
        prompt: str,
        temperature: float,
        top_p: float,
        top_k: int,
        max_new_tokens: int = 512,
    ) -> str:
        res = self.model.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpfull ai assistant who give answer to user queries. answer must be short as possible and simple.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            max_tokens=max_new_tokens,
            stream=True,
        )

        print(
            f"Inference params: \n{temperature=}\n{top_p=}\n{top_k=}\n{max_new_tokens=}"
        )

        print("Assistant", end=" : ")
        for token in res:
            print(token["choices"][0]["delta"].get("content", ""), flush=True, end="")
        print(" ")
