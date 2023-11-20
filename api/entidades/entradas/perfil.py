from datetime import date

from api.entidades import Modelo
from banco.tabelas.perfil import Genero, TipoSanguineo


class PerfilEntrada(Modelo):
    """
    ## São os dados necessários para criar um perfil.

    Separamos entrada e saída para facilitar a validação.
    """

    nome: str
    data_nascimento: date
    tipo_sanguineo: TipoSanguineo
    genero: Genero
    alergias_e_restricoes: list[str]


class PerfilEntradaOpcional(Modelo):
    """
    ## A mesma coisa que `PerfilEntrada`, mas com campos opcionais.

    Necessário para atualizar um perfil de forma parcial.
    """

    nome: str | None = None
    data_nascimento: date | None = None
    tipo_sanguineo: TipoSanguineo | None = None
    genero: Genero | None = None
    alergias_e_restricoes: list[str] | None = None
