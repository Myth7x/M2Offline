"""
M2Offline Database Manager
Author: Myth
----------------------
Ich dachte mir es wird SQLite genutzt, da es sehr einfach zu bedienen ist und
auch sehr schnell ist. Ich habe eine kleine Klasse erstellt, die die Tabellen
erstellt. Die Tabellen werden in der Klasse Schema definiert. Die Tabellen
werden in der Datei database.db gespeichert. Die Klasse Schema kann beliebig
erweitert werden. Die Tabellen werden beim ersten Starten der Anwendung
erstellt. Wenn die Datei database.db geloescht wird, werden die Tabellen
wieder erstellt.
"""
import logging
from typing import Any
import sqlalchemy as sa

from .schema            import Accounts, Characters
from .extended_base     import ExtendedBase
from .session_manager   import SessionManager
from .                  import utils
# - - - - - - - - - - - - - - - - - - - -
"""
    Create Schema function 
    (this gets called from binary after executing prototype.py->database_manager.InitializePython(..))
"""
def CreateSchema(module):
    try:
        engine = sa.create_engine("sqlite:///database.db", echo=False)
        extended_base.Base.metadata.create_all(engine)
        utils.Commit(engine)
        logging.getLogger('[Database]').info("Schema created")
    except Exception as e:
        logging.getLogger('[Database]').error("Error while creating schema: %s", e)

"""
    Query with return fetchall
"""
def QueryWithReturn(_connection, query):
    try:
        result = _connection.execute(sa.text(query))
        _connection.commit()
        return result.fetchall()
    except Exception as e:
        _connection.rollback()
        return None
