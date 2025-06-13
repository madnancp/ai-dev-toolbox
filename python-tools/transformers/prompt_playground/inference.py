from typing import Any, List, Dict
from transformers import AutoModelForCausalLM, AutoTokenizer


class LLMInferenceManager:

    def __init__(self, model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0") -> None:
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name, torch_dtype="auto", device_map="auto"
        )

    def ask(self, query: str) -> str:
        pass

    def pass_query(self, query: str) -> Any:
        prompt = self._set_chat_template(query)
        token_ids = self.tokenizer.add_chat_template(prompt, return_tensors="pt")
        self.model(**token_ids)

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
