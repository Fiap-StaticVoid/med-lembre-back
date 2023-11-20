from datetime import date

from sqlalchemy.orm import Mapped

from banco.tabelas import TabelaBase


class Registro(TabelaBase):
    __tablename__ = "registros"

    titulo: Mapped[str]
    data: Mapped[date]
    observacoes: Mapped[str]

    def para_dicionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "data": self.data,
            "observacoes": self.observacoes,
        }
