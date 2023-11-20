from uuid import UUID

from api.entidades.entradas.perfil import PerfilEntrada


class PerfilResposta(PerfilEntrada):
    id: UUID
