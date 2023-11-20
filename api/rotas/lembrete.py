from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.entidades.entradas.lembrete import LembreteEntrada, LembreteEntradaOpcional
from api.entidades.saidas.lembrete import LembreteResposta
from banco import abrir_sessao
from banco.repositorios import Repositorio
from banco.tabelas.lembrete import Lembrete

lembrete_router = APIRouter(prefix="/lembretes", tags=["Lembretes"])
repo_lembrete = Repositorio[
    LembreteEntrada,
    LembreteEntradaOpcional,
    Lembrete,
]


def abrir_repo_lembrete(sessao: AsyncSession = Depends(abrir_sessao)):
    repo: repo_lembrete = Repositorio(sessao, Lembrete)
    return repo


@lembrete_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=LembreteResposta,
    summary="Cria um novo lembrete",
)
async def criar_lembrete(
    lembrete: LembreteEntrada, repo: repo_lembrete = Depends(abrir_repo_lembrete)
):
    _lembrete = await repo.criar(lembrete)
    return _lembrete.para_dicionario()


@lembrete_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[LembreteResposta],
    summary="Lista todos os lembretes",
)
async def listar_lembretes(repo: repo_lembrete = Depends(abrir_repo_lembrete)):
    lembretes = await repo.listar()
    return [lembrete.para_dicionario() for lembrete in lembretes]


@lembrete_router.get(
    "/{lembrete_id}",
    status_code=status.HTTP_200_OK,
    response_model=LembreteResposta,
    summary="Busca um lembrete pelo ID",
)
async def buscar_lembrete(
    lembrete_id: UUID, repo: repo_lembrete = Depends(abrir_repo_lembrete)
):
    _lembrete = await repo.obter(lembrete_id)
    return _lembrete.para_dicionario()


@lembrete_router.patch(
    "/{lembrete_id}",
    status_code=status.HTTP_200_OK,
    response_model=LembreteResposta,
    summary="Atualiza um lembrete pelo ID",
)
async def atualizar_lembrete(
    lembrete_id: UUID,
    lembrete: LembreteEntradaOpcional,
    repo: repo_lembrete = Depends(abrir_repo_lembrete),
):
    _lembrete = await repo.atualizar(lembrete_id, lembrete)
    return _lembrete.para_dicionario()


@lembrete_router.delete(
    "/{lembrete_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apaga um lembrete pelo ID",
)
async def apagar_lembrete(
    lembrete_id: UUID, repo: repo_lembrete = Depends(abrir_repo_lembrete)
):
    await repo.remover(lembrete_id)
