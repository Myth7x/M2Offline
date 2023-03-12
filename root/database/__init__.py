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

import database_manager as dbMgr

from .schema            import Account, Player
from .extended_base     import ExtendedBase
from .session_manager   import SessionManager
# - - - - - - - - - - - - - - - - - - - -
"""
    Create Schema function 
    (this gets called from binary after executing prototype.py->database_manager.InitializePython(..))
"""
def CreateSchema(_engine):
    try:
        with _engine.connect() as _connection: # To automatically close connection
            _session_manager = SessionManager(_engine)
            with _session_manager as session: # To automatically commit or rollback
                ExtendedBase.metadata.create_all(_engine)
        _engine.dispose()
    except Exception as e:
        logging.exception("Failed to create database schema")
        raise e

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
