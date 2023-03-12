import logging
import sqlalchemy as sa

logger = {
	"Aethernum" 	: logging.getLogger('[Aethernum]'),
	"Database" 		: logging.getLogger('[Database]')
}

# 1. Init python module : Binary -> Python | Python -> Binary
########################################
## Setup database, set module ptr to db manager
logger["Database"].info("Loading Database...")

import database_manager as dbMgr
import database as db_module

_engine = sa.create_engine(dbMgr.DB_NAME, echo=False)
dbMgr.InitializePython(db_module, _engine)				# Binary -> Python + Create Schema


########################################
with _engine.connect() as _connection:
	_session_manager = db_module.session_manager.SessionManager(_engine)
	with _session_manager as session:
		session.add(db_module.schema.Account(name="Myth", hash="1234"))
	logger["Database"].info("Result: %s", db_module.QueryWithReturn(_connection, "SELECT * FROM Account"))
########################################

import app, wndmgr, systemsetting, dbg



import ui
from phase_manager import PhaseManager
def RunApp():
	app.SetHairColorEnable(1)
	app.SetArmorSpecularEnable(1)
	app.SetWeaponSpecularEnable(1)
	wndmgr.SetScreenSize(systemsetting.GetWidth(), systemsetting.GetHeight())
	app.Create("M2😀ffline", systemsetting.GetWidth(), systemsetting.GetHeight(), 1)
	app.SetCamera(1500.0, 30.0, 0.0, 180.0)
	app.LoadLocaleData(app.GetLocalePath())
	phase_manager = PhaseManager()
	phase_manager.SetLoginPhase()
	app.Loop()
	phase_manager.Destroy()


RunApp()

