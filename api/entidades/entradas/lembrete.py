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
