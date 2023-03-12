import sqlalchemy.ext.declarative as sa_declarative
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class ExtendedBase(Base):
    __abstract__ = True
    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __repr__(self) -> str:
        return "<{}>".format(self.__class__.__name__)