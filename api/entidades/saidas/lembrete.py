from uuid import UUID

from api.entidades.entradas.lembrete import LembreteEntrada


class LembreteResposta(LembreteEntrada):
    id: UUID
