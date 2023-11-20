from datetime import time

from api.entidades import Modelo
from banco.tabelas.lembrete import Recorrencia


class LembreteEntrada(Modelo):
    """
    ## São os dados necessários para criar um lembrete.

    Separamos entrada e saída para facilitar a validação.
    """

    titulo: str
    hora_inicio: time
    intervalo: int
    intervalo_tipo: Recorrencia
    duracao: int
    duracao_tipo: Recorrencia
    concluido: bool


class LembreteEntradaOpcional(Modelo):
    """
    ## A mesma coisa que `LembreteEntrada`, mas com campos opcionais.

    Necessário para atualizar um lembrete de forma parcial.
    """

    titulo: str | None = None
    hora_inicio: time | None = None
    intervalo: int | None = None
    intervalo_tipo: Recorrencia | None = None
    duracao: int | None = None
    duracao_tipo: Recorrencia | None = None
    concluido: bool | None = None
