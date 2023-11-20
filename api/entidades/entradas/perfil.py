from datetime import date

from api.entidades import Modelo
from banco.tabelas.perfil import Genero, TipoSanguineo


class PerfilEntrada(Modelo):
    nome: str
    data_nascimento: date
    tipo_sanguineo: TipoSanguineo
    genero: Genero
    alergias_e_restricoes: list[str]