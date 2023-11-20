from datetime import date

from api.entidades import Modelo


class RegistroEntrada(Modelo):
    """
    ## São os dados necessários para criar um registro.

    Separamos entrada e saída para facilitar a validação.
    """

    titulo: str
    data: date
    observacoes: str


class RegistroEntradaOpcional(Modelo):
    """
    ## A mesma coisa que `RegistroEntrada`, mas com campos opcionais.

    Necessário para atualizar um registro de forma parcial.
    """

    titulo: str | None = None
    data: date | None = None
    observacoes: str | None = None
