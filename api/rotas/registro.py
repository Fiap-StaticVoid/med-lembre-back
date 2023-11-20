from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.entidades.entradas.registro import RegistroEntrada, RegistroEntradaOpcional
from api.entidades.saidas.registro import RegistroResposta
from banco import abrir_sessao
from banco.repositorios import Repositorio
from banco.tabelas.registro import Registro

registro_router = APIRouter(prefix="/registros", tags=["Registros"])
repo_registro = Repositorio[
    RegistroEntrada,
    RegistroEntradaOpcional,
    Registro,
]


def abrir_repo_perfil(sessao: AsyncSession = Depends(abrir_sessao)):
    repo: repo_registro = Repositorio(sessao, Registro)
    return repo


@registro_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=RegistroResposta,
    summary="Cria um novo registro",
)
async def criar_registro(
    registro: RegistroEntrada, repo: repo_registro = Depends(abrir_repo_perfil)
):
    _registro = await repo.criar(registro)
    return _registro.para_dicionario()


@registro_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[RegistroResposta],
    summary="Lista todos os registros",
)
async def listar_registros(repo: repo_registro = Depends(abrir_repo_perfil)):
    registros = await repo.listar()
    return [registro.para_dicionario() for registro in registros]


@registro_router.get(
    "/{registro_id}",
    status_code=status.HTTP_200_OK,
    response_model=RegistroResposta,
    summary="Busca um registro pelo ID",
)
async def buscar_registro(
    registro_id: UUID, repo: repo_registro = Depends(abrir_repo_perfil)
):
    _registro = await repo.obter(registro_id)
    return _registro.para_dicionario()


@registro_router.patch(
    "/{registro_id}",
    status_code=status.HTTP_200_OK,
    response_model=RegistroResposta,
    summary="Atualiza um registro pelo ID",
)
async def atualizar_registro(
    registro_id: UUID,
    registro: RegistroEntradaOpcional,
    repo: repo_registro = Depends(abrir_repo_perfil),
):
    _registro = await repo.atualizar(registro_id, registro)
    return _registro.para_dicionario()


@registro_router.delete(
    "/{registro_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apaga um registro pelo ID",
)
async def apagar_registro(
    registro_id: UUID, repo: repo_registro = Depends(abrir_repo_perfil)
):
    await repo.remover(registro_id)
    return None
