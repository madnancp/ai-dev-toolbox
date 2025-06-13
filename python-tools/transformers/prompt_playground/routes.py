from fastapi import APIRouter
from pydantic import BaseModel


class PromptSchema(BaseModel):
    prompt: str
    temperature: float
    top_k: int
    top_p: float


router = APIRouter(tags=["inference"])


@router.post("/generate")
def get_llm_reponse(prompt: PromptSchema):
    return {"result": "Capital of India is New Delhi."}
