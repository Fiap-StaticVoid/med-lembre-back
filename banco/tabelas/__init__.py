from typing import Annotated
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

UUID_PK = Annotated[UUID, mapped_column(default=uuid4, primary_key=True)]


class Base(DeclarativeBase):
    pass


class TabelaBase(AbstractConcreteBase, Base):
    id: Mapped[UUID_PK]
