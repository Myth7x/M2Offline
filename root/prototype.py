import logging
import sqlalchemy as sa

logger = {
	"Aethernum" 	: logging.getLogger('[Aethernum]'),
	"Database" 		: logging.getLogger('[Database]')
}


import ui
from phase_manager import PhaseManager
phase_manager = PhaseManager()

# 1. Init python module : Binary -> Python | Python -> Binary
########################################
## Setup database, set module ptr to db manager
logger["Database"].info("Loading Database...")

import database_manager as dbMgr
import database as db_module

engine = sa.create_engine(dbMgr.DB_NAME, echo=False)
dbMgr.InitializePython(db_module, engine, phase_manager)				# Binary -> Python + Create Schema

import app, wndmgr, systemsetting, dbg


def RunApp(engine):
	app.SetHairColorEnable(1)
	app.SetArmorSpecularEnable(1)
	app.SetWeaponSpecularEnable(1)
	wndmgr.SetScreenSize(systemsetting.GetWidth(), systemsetting.GetHeight())
	app.Create("M2😀ffline", systemsetting.GetWidth(), systemsetting.GetHeight(), 1)
	app.SetCamera(1500.0, 30.0, 0.0, 180.0)
	app.LoadLocaleData(app.GetLocalePath())
	phase_manager.SetLoginPhase()
	app.Loop()
	phase_manager.Destroy()


#RunApp()


########################################
with engine.connect() as _connection:
	logging.getLogger('init').info("Connected to database")
	RunApp(engine)
	engine.dispose()


