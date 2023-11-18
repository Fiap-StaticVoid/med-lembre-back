from datetime import date

from sqlalchemy.orm import Mapped

from banco.tabelas import TabelaBase


class Registro(TabelaBase):
    titulo: Mapped[str]
    data: Mapped[date]
    observacoes: Mapped[str]
