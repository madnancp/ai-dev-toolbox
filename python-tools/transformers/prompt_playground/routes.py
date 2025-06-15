from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel


class PromptSchema(BaseModel):
    prompt: str
    max_new_tokens: int
    temperature: float
    top_k: int
    top_p: float


router = APIRouter(tags=["inference"])


@router.post("/generate")
async def get_streaming_output(request: Request, prompt: PromptSchema):
    res = request.app.state.llm_inference
    return StreamingResponse(
        res.streaming_output(
            prompt.prompt,
            prompt.temperature,
            prompt.max_new_tokens,
            prompt.top_p,
            prompt.top_k,
        ),
        media_type="text/plain",
    )
