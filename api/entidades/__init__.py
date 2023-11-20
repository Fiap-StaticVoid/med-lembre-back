from pydantic import BaseModel, ConfigDict


def snake_para_camel(texto: str) -> str:
    inicio, *resto = texto.split("_")
    return "".join([inicio.lower(), *map(str.title, resto)])


class Modelo(BaseModel):
    model_config = ConfigDict(alias_generator=snake_para_camel)
