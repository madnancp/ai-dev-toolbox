from contextlib import contextmanager
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from prompt_playground.inference import LLMInferenceManager


class PromptSchema(BaseModel):
    prompt: str
    temperature: float
    top_k: int
    top_p: float


llm_inference: None | LLMInferenceManager = None


@contextmanager
async def lifespan(app: FastAPI):
    global llm_inference
    llm_inference = LLMInferenceManager()
    yield


router = APIRouter(tags=["inference"])


@router.post("/generate")
def get_llm_reponse(prompt: PromptSchema):
    if llm_inference is not None:
        llm_inference.ask(prompt.prompt)
    return {"result": "Capital of India is New Delhi."}
