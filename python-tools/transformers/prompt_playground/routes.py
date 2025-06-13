from fastapi import APIRouter, Request
from pydantic import BaseModel


class PromptSchema(BaseModel):
    prompt: str
    max_new_tokens: int
    temperature: float
    top_k: int
    top_p: float


router = APIRouter(tags=["inference"])


@router.post("/generate")
async def get_llm_reponse(request: Request, prompt: PromptSchema):
    res = request.app.state.llm_inference
    out = await res.ask(
        prompt.prompt,
        prompt.temperature,
        prompt.max_new_tokens,
        prompt.top_p,
        prompt.top_k,
    )
    return {"result": out}
