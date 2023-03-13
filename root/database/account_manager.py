import database_manager as dbMgr
from .schema            import Account, Player
from . import logging

_engine = dbMgr.GetEngine()
logging.getLogger('[Database]').info("Result: %s", dbMgr.QueryWithReturn(_engine, "SELECT * FROM Account"))