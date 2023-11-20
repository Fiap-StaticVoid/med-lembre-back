from uuid import UUID

from fastapi import APIRouter, status

from api.entidades.entradas.lembrete import LembreteEntrada
from api.entidades.saidas.lembrete import LembreteResposta

lembrete_router = APIRouter(prefix="/lembretes", tags=["Lembretes"])


@lembrete_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=LembreteResposta,
    summary="Cria um novo lembrete",
)
def criar_lembrete(lembrete: LembreteEntrada):
    pass


@lembrete_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[LembreteResposta],
    summary="Lista todos os lembretes",
)
def listar_lembretes():
    pass


@lembrete_router.get(
    "/{lembrete_id}",
    status_code=status.HTTP_200_OK,
    response_model=LembreteResposta,
    summary="Busca um lembrete pelo ID",
)
def buscar_lembrete(lembrete_id: UUID):
    pass


@lembrete_router.patch(
    "/{lembrete_id}",
    status_code=status.HTTP_200_OK,
    response_model=LembreteResposta,
    summary="Atualiza um lembrete pelo ID",
)
def atualizar_lembrete(lembrete_id: UUID, lembrete: LembreteEntrada):
    pass


@lembrete_router.delete(
    "/{lembrete_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apaga um lembrete pelo ID",
)
def apagar_lembrete(lembrete_id: UUID):
    pass
