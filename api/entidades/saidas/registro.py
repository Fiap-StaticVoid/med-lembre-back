from uuid import UUID

from api.entidades.entradas.registro import RegistroEntrada


class RegistroResposta(RegistroEntrada):
    """
    ## São os dados retornados ao criar um registro.

    A resposta é igual à entrada, mas com o ID.
    """

    id: UUID
