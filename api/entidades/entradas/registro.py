from datetime import date

from api.entidades import Modelo


class RegistroEntrada(Modelo):
    titulo: str
    data: date
    observacoes: str
