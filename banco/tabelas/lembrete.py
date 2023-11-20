from datetime import time
from enum import StrEnum

from sqlalchemy.orm import Mapped

from banco.tabelas import TabelaBase


class Recorrencia(StrEnum):
    HORARIO = "horario"
    DIARIO = "diario"
    SEMANAL = "semanal"
    MENSAL = "mensal"
    ANUAL = "anual"


def converter_recorrencia(valor: int, tipo: Recorrencia) -> int:
    _valor = valor
    match tipo:
        case None:
            raise ValueError("Tipo de recorrência não informado")
        case Recorrencia.HORARIO:
            pass
        case _:
            _valor *= 24

    match tipo:
        case Recorrencia.HORARIO:
            return _valor
        case Recorrencia.DIARIO:
            return valor
        case Recorrencia.SEMANAL:
            return valor * 7
        case Recorrencia.MENSAL:
            return valor * 30
        case Recorrencia.ANUAL:
            return valor * 365


class Lembrete(TabelaBase):
    __tablename__ = "lembretes"

    titulo: Mapped[str]
    hora_inicio: Mapped[time]
    intervalo: Mapped[int]
    intervalo_tipo: Mapped[Recorrencia]
    duracao: Mapped[int]
    duracao_tipo: Mapped[Recorrencia]
    concluido: Mapped[bool]

    @property
    def total_de_lembretes(self) -> int:
        intervalo = converter_recorrencia(self.intervalo, self.intervalo_tipo)
        duracao = converter_recorrencia(self.duracao, self.duracao_tipo)

        return duracao // intervalo

    def para_dicionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "hora_inicio": self.hora_inicio,
            "intervalo": self.intervalo,
            "intervalo_tipo": self.intervalo_tipo,
            "duracao": self.duracao,
            "duracao_tipo": self.duracao_tipo,
            "concluido": self.concluido,
        }
