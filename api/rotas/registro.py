from uuid import UUID

from fastapi import APIRouter, status

from api.entidades.entradas.registro import RegistroEntrada
from api.entidades.saidas.registro import RegistroResposta

registro_router = APIRouter(prefix="/registros", tags=["Registros"])


@registro_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=RegistroResposta,
    summary="Cria um novo registro",
)
def criar_registro(registro: RegistroEntrada):
    pass


@registro_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[RegistroResposta],
    summary="Lista todos os registros",
)
def listar_registros():
    pass


@registro_router.get(
    "/{registro_id}",
    status_code=status.HTTP_200_OK,
    response_model=RegistroResposta,
    summary="Busca um registro pelo ID",
)
def buscar_registro(registro_id: UUID):
    pass


@registro_router.patch(
    "/{registro_id}",
    status_code=status.HTTP_200_OK,
    response_model=RegistroResposta,
    summary="Atualiza um registro pelo ID",
)
def atualizar_registro(registro_id: UUID, registro: RegistroEntrada):
    pass


@registro_router.delete(
    "/{registro_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apaga um registro pelo ID",
)
def apagar_registro(registro_id: UUID):
    pass
