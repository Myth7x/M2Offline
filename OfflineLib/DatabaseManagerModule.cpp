#include "StdAfx.h"
#include "DatabaseManager.h"

PyObject* dbgMgrExecute(PyObject* poSelf, PyObject* poArgs)
{
	std::wstring query;
	if (!PyTuple_GetWString(poArgs, 0, query))
		return Py_BuildException();

	std::map<int, std::wstring> res = CDatabaseManager::Instance().Execute(query);
}

PyObject* dbgMgrInitializePython(PyObject* poSelf, PyObject* poArgs)
{
	PyObject* poModule;
	if (!PyTuple_GetObject(poArgs, 0, &poModule))
		return Py_BuildException();

	CDatabaseManager::Instance().InitPython(poModule);

	return Py_BuildNone();
}


PyMODINIT_FUNC initdatabasemanager()
{
	static PyMethodDef s_methods[] =
	{
		{ ObfStr("InitializePython"), dbgMgrInitializePython, METH_VARARGS },
		{ ObfStr("Execute"), dbgMgrExecute, METH_VARARGS },

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
	
	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	return poModule;
}
