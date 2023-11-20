from uuid import UUID

from api.entidades.entradas.registro import RegistroEntrada


class RegistroResposta(RegistroEntrada):
    id: UUID
