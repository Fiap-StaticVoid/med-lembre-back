from uuid import UUID

from fastapi import APIRouter, status

from api.entidades.entradas.perfil import PerfilEntrada
from api.entidades.saidas.perfil import PerfilResposta

perfil_router = APIRouter(prefix="/perfis", tags=["Perfis"])


@perfil_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=PerfilResposta,
    summary="Cria um novo perfil",
)
def criar_perfil(perfil: PerfilEntrada):
    pass


@perfil_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[PerfilResposta],
    summary="Lista todos os perfis",
)
def listar_perfis():
    pass


@perfil_router.get(
    "/{perfil_id}",
    status_code=status.HTTP_200_OK,
    response_model=PerfilResposta,
    summary="Busca um perfil pelo ID",
)
def buscar_perfil(perfil_id: UUID):
    pass


@perfil_router.patch(
    "/{perfil_id}",
    status_code=status.HTTP_200_OK,
    response_model=PerfilResposta,
    summary="Atualiza um perfil pelo ID",
)
def atualizar_perfil(perfil_id: UUID, perfil: PerfilEntrada):
    pass


@perfil_router.delete(
    "/{perfil_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apaga um perfil pelo ID",
)
def apagar_perfil(perfil_id: UUID):
    pass
