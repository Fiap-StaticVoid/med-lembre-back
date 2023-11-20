from datetime import date
from enum import StrEnum

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from banco.tabelas import TabelaBase


class TipoSanguineo(StrEnum):
    A_POSITIVO = "a+"
    A_NEGATIVO = "a-"
    B_POSITIVO = "b+"
    B_NEGATIVO = "b-"
    AB_POSITIVO = "ab+"
    AB_NEGATIVO = "ab-"
    O_POSITIVO = "o+"
    O_NEGATIVO = "o-"


class Genero(StrEnum):
    MASCULINO = "masculino"
    FEMININO = "feminino"
    NAO_BINARIO = "nao binario"
    NAO_INFORMAR = "nao informar"


class Perfil(TabelaBase):
    __tablename__ = "perfis"

    nome: Mapped[str]
    data_nascimento: Mapped[date]
    tipo_sanguineo: Mapped[TipoSanguineo]
    genero: Mapped[Genero]
    alergias_e_restricoes: Mapped[list[str]] = mapped_column(ARRAY(String))

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "tipo_sanguineo": self.tipo_sanguineo,
            "genero": self.genero,
            "alergias_e_restricoes": self.alergias_e_restricoes,
        }
