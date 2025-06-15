from typing import Any, List, Dict
from transformers import AutoModelForCausalLM, AutoTokenizer


class LLMInferenceManager:

    def __init__(self, model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0") -> None:
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name, torch_dtype="auto", device_map="auto"
        )

    async def ask(
        self,
        query: str,
        temperature: float,
        max_new_tokens: int,
        top_p: float,
        top_k: int,
    ) -> str:
        model_out = await self.pass_query(
            query, temperature, max_new_tokens, top_p, top_k
        )
        result = await self.decode_output_ids(model_out)

        return self._format_output(result)

    async def pass_query(
        self,
        query: str,
        temperature: float,
        max_new_tokens: int,
        top_p: float,
        top_k: int,
    ) -> Any:
        prompt = self._set_chat_template(query)
        token_ids = self.tokenizer.apply_chat_template(
            prompt, return_tensors="pt", tokenize=True
        )
        output_ids = self.model.generate(
            token_ids,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            top_p=top_p,
            top_k=top_k,
            do_sample=True,
        )
        return output_ids[0]

    def streaming_output(
        self,
        query: str,
        temperature: float,
        max_new_tokens: int,
        top_p: float,
        top_k: int,
    ):
        from threading import Thread
        from transformers.generation.streamers import TextIteratorStreamer

        streamer = TextIteratorStreamer(
            self.tokenizer, skip_prompt=True, skip_special_tokens=True
        )
        message = self._set_chat_template(query)
        text = self.tokenizer.apply_chat_template(
            message, tokenize=False, add_generation_prompt=True
        )

        input_id = self.tokenizer(text, return_tensors="pt")

        model_kwargs = dict(
            input_ids=input_id["input_ids"],
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            do_sample=True,
            max_new_tokens=max_new_tokens,
            streamer=streamer,
        )

        streaming_thread = Thread(target=self.model.generate, kwargs=model_kwargs)

        streaming_thread.start()

        for token in streamer:
            if token != "":
                print(token, end="", flush=True)
                yield token

    async def decode_output_ids(self, token_ids: Any) -> str:
        return self.tokenizer.decode(token_ids, skip_special_tokens=True)

    def _set_chat_template(self, query: str) -> List[Dict[str, str]]:
        messages = [
            {
                "role": "system",
                "content": "you're a helpfull AI assistant who reply answer to the user query with humble and kindness.",
            },
            {
                "role": "user",
                "content": query,
            },
        ]
        return messages

    def _format_output(self, output: str) -> str:
        """return only ai generated result."""

        if "<|assistant|>" in output:
            result = output.split("<|assistant|>")[1]
            return result.strip()

        return output.strip()
