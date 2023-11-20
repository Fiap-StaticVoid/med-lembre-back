from uuid import UUID

from api.entidades.entradas.lembrete import LembreteEntrada


class LembreteResposta(LembreteEntrada):
    """
    ## São os dados retornados ao criar um lembrete.

    A resposta é igual à entrada, mas com o ID.
    """

    id: UUID
