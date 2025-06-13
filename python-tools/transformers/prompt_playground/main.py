from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from prompt_playground.routes import router
from prompt_playground.inference import LLMInferenceManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    infr = LLMInferenceManager()
    app.state.llm_inference = infr

    yield

    del app.state.llm_inference


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

app.include_router(router, prefix="/api/v1")
