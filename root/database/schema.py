"""
Schema for the database
Using SQLAlchemy Base as base class
"""

import sqlalchemy as sa
from .extended_base import ExtendedBase
from .types import CharacterRace

class Accounts(ExtendedBase):
    __tablename__ = "Accounts"
    __table_args__ = {}    
    id      = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name    = sa.Column(sa.String(255))
    hash    = sa.Column(sa.String(255))
    def __init__(self, **kwargs):
        self.update(**kwargs)

class Characters(ExtendedBase):
    __tablename__ = "Characters"
    __table_args__ = {}
    id      = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name    = sa.Column(sa.String(255))
    account = sa.Column(sa.Integer, sa.ForeignKey("Accounts.id"))
    race    = sa.Column(sa.Integer, default=CharacterRace.WARRIOR_MALE)
    job     = sa.Column(sa.Integer, default=0)
    exp     = sa.Column(sa.Integer, default=0)
    def __init__(self, **kwargs):
        self.update(**kwargs)