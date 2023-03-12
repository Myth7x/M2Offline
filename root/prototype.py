import logging
import sqlalchemy as sa

logger = {
	"Aethernum" : logging.getLogger('[Aethernum]'),
	"Database" : logging.getLogger('[Database]')
}

# 1. Init python module : Binary -> Python | Python -> Binary
########################################
## Setup database, set module ptr to db manager
import database_manager as dbMgr
import database as db_module
dbMgr.InitializePython(db_module)
########################################

logger["Database"].info("Loading Database...")

_engine = sa.create_engine("sqlite:///database.db", echo=False)

with _engine.connect() as _connection:
	_session_manager = db_module.session_manager.SessionManager(_engine)

	# Using the session manager
	with _session_manager as session:
		# Create a new account
		session.add(db_module.schema.Accounts(name="Myth", hash="1234"))
		session.commit()

	# Using the logger to query the database and look at the account table
	logger["Database"].info("Result: %s", db_module.QueryWithReturn(_connection, "SELECT * FROM Accounts"))

####################

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

