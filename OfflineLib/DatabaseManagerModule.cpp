#include "StdAfx.h"
#include "DatabaseManager.h"

PyObject* dbMgrExecute(PyObject* poSelf, PyObject* poArgs)
{
	std::wstring query;
	if (!PyTuple_GetWString(poArgs, 0, query))
		return Py_BuildException();

	std::map<int, std::wstring> res = CDatabaseManager::Instance().Execute(query);
}

PyObject* dbMgrInitializePython(PyObject* poSelf, PyObject* poArgs)
{
	PyObject* poModule;
	if (!PyTuple_GetObject(poArgs, 0, &poModule))
		return Py_BuildException();

	PyObject* poEngine;
	if (!PyTuple_GetObject(poArgs, 1, &poEngine))
		return Py_BuildException();

	PyObject* poPhaseManager;
	if (!PyTuple_GetObject(poArgs, 2, &poPhaseManager))
		return Py_BuildException();

	CDatabaseManager::Instance().InitPython(poModule, poEngine, poPhaseManager);

	return Py_BuildNone();
}

PyObject* dbMgrGetEngine(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("O", CDatabaseManager::Instance().GetEngine());
}

PyObject* dbMgrGetPhaseManager(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("O", CDatabaseManager::Instance().GetPhaseManager());
}

PyMODINIT_FUNC initdatabasemanager()
{
	static PyMethodDef s_methods[] =
	{
		{ ObfStr("InitializePython"), dbMgrInitializePython, METH_VARARGS },
		{ ObfStr("Execute"), dbMgrExecute, METH_VARARGS },
		{ ObfStr("GetPhaseManager"), dbMgrGetPhaseManager, METH_VARARGS },
		{ ObfStr("GetEngine"), dbMgrGetEngine, METH_VARARGS },

		{ NULL, NULL, NULL },
	};

	static struct PyModuleDef moduledef = {
		PyModuleDef_HEAD_INIT,
		"database_manager",
		NULL,
		-1,
		s_methods
	};

	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	PyObject* poModule = PyModule_Create(&moduledef);
	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	PyModule_AddStringConstant(poModule, ObfStr("DB_NAME"), "sqlite:///database.db");
	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	return poModule;
}
