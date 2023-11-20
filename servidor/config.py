from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from api.rotas.lembrete import lembrete_router
from api.rotas.perfil import perfil_router
from api.rotas.registro import registro_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    from banco import iniciar_banco

    await iniciar_banco()
    yield


app = FastAPI(lifespan=lifespan)
origens = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origens,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse("/docs")


app.include_router(perfil_router)
app.include_router(lembrete_router)
app.include_router(registro_router)
