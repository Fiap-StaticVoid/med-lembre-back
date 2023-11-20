from datetime import date

from api.entidades import Modelo


class RegistroEntrada(Modelo):
    titulo: str
    data: date
    observacoes: str


class RegistroEntradaOpcional(Modelo):
    titulo: str | None = None
    data: date | None = None
    observacoes: str | None = None
