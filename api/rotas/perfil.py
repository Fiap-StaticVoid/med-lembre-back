from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.entidades.entradas.perfil import PerfilEntrada, PerfilEntradaOpcional
from api.entidades.saidas.perfil import PerfilResposta
from banco import abrir_sessao
from banco.repositorios import Repositorio
from banco.tabelas.perfil import Perfil

perfil_router = APIRouter(prefix="/perfis", tags=["Perfis"])
repo_perfil = Repositorio[
    PerfilEntrada,
    PerfilEntradaOpcional,
    Perfil,
]


def abrir_repo_perfil(sessao: AsyncSession = Depends(abrir_sessao)):
    repo: repo_perfil = Repositorio(sessao, Perfil)
    return repo


@perfil_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=PerfilResposta,
    summary="Cria um novo perfil",
)
async def criar_perfil(
    perfil: PerfilEntrada, repo: repo_perfil = Depends(abrir_repo_perfil)
):
    _perfil = await repo.criar(perfil)
    return _perfil.para_dicionario()


@perfil_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[PerfilResposta],
    summary="Lista todos os perfis",
)
async def listar_perfis(repo: repo_perfil = Depends(abrir_repo_perfil)):
    perfis = await repo.listar()
    return [perfil.para_dicionario() for perfil in perfis]


@perfil_router.get(
    "/{perfil_id}",
    status_code=status.HTTP_200_OK,
    response_model=PerfilResposta,
    summary="Busca um perfil pelo ID",
)
async def buscar_perfil(
    perfil_id: UUID, repo: repo_perfil = Depends(abrir_repo_perfil)
):
    _perfil = await repo.obter(perfil_id)
    return _perfil.para_dicionario()


@perfil_router.patch(
    "/{perfil_id}",
    status_code=status.HTTP_200_OK,
    response_model=PerfilResposta,
    summary="Atualiza um perfil pelo ID",
)
async def atualizar_perfil(
    perfil_id: UUID,
    perfil: PerfilEntradaOpcional,
    repo: repo_perfil = Depends(abrir_repo_perfil),
):
    _perfil = await repo.atualizar(perfil_id, perfil)
    return _perfil.para_dicionario()


@perfil_router.delete(
    "/{perfil_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apaga um perfil pelo ID",
)
async def apagar_perfil(
    perfil_id: UUID, repo: repo_perfil = Depends(abrir_repo_perfil)
):
    await repo.remover(perfil_id)
