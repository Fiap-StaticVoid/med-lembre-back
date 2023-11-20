from uuid import UUID

from api.entidades.entradas.perfil import PerfilEntrada


class PerfilResposta(PerfilEntrada):
    """
    ## São os dados retornados ao criar um perfil.

    A resposta é igual à entrada, mas com o ID.
    """

    id: UUID
