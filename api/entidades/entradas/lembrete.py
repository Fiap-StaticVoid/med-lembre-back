from datetime import time

from api.entidades import Modelo
from banco.tabelas.lembrete import Recorrencia


class LembreteEntrada(Modelo):
    titulo: str
    hora_inicio: time
    intervalo: int
    intervalo_tipo: Recorrencia
    duracao: int
    duracao_tipo: Recorrencia
    concluido: bool


class LembreteEntradaOpcional(Modelo):
    titulo: str | None = None
    hora_inicio: time | None = None
    intervalo: int | None = None
    intervalo_tipo: Recorrencia | None = None
    duracao: int | None = None
    duracao_tipo: Recorrencia | None = None
    concluido: bool | None = None
