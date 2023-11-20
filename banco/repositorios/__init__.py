from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar

from sqlalchemy import UUID, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from api.entidades import Modelo
from banco.tabelas import TabelaBase

E = TypeVar("E", bound=Modelo)
EO = TypeVar("EO", bound=Modelo)
M = TypeVar("M", bound=TabelaBase)


@dataclass
class Repositorio(Generic[E, EO, M]):
    sessao: AsyncSession
    modelo: type[M]

    async def criar(self, entidade: E) -> M:
        instancia = self.modelo(**entidade.model_dump())
        self.sessao.add(instancia)
        await self.sessao.commit()
        return instancia

    async def listar(self) -> Iterator[M]:
        return await self.sessao.scalars(select(self.modelo))

    async def obter(self, id_: UUID) -> M:
        return await self.sessao.scalar(
            select(self.modelo).where(self.modelo.id == id_)
        )

    async def atualizar(self, id_: UUID, entidade: EO) -> M:
        instancia = await self.obter(id_)
        for campo, valor in entidade.model_dump().items():
            if valor is None:
                continue
            setattr(instancia, campo, valor)
        await self.sessao.commit()
        return instancia

    async def remover(self, id_: UUID) -> None:
        await self.sessao.execute(delete(self.modelo).where(self.modelo.id == id_))
        await self.sessao.commit()
