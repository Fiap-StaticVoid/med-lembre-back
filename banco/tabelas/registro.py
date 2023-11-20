from datetime import date

from sqlalchemy.orm import Mapped

from banco.tabelas import TabelaBase


class Registro(TabelaBase):
    """
    ## Representa um registro no banco de dados.

    O registro é usado para armazenar informações passadas do usuário.
    Um exemplo de uso é para armazenar informações de consultas passadas.
    Outro exemplo de uso é para armazenar informações de problemas de saúde.
    """

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
