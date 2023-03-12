#include "StdAfx.h"
#include "DatabaseManager.h"

CDatabaseManager::CDatabaseManager()
{}

CDatabaseManager::~CDatabaseManager()
{}

std::map<int, std::wstring> CDatabaseManager::Execute(std::wstring& query)
{
    std::map<int, std::wstring> ret;
    if (!m_ppyDatabase)
        return ret;

    long retPtr = PyCallClassMemberFunc(m_ppyDatabase, "Execute", Py_BuildValue("(s)", query.c_str()));
    PyObject* poRet = (PyObject*)&retPtr;
    
    if (PyDict_Check(poRet))
    {
        PyObject* poKey;
        PyObject* poValue;
        Py_ssize_t pos = 0;

        while (PyDict_Next(poRet, &pos, &poKey, &poValue))
        {
            int key = PyLong_AsLong(poKey);
            auto value = PyByteArray_AsString(poValue);
            std::wstring wvalue(value, value + strlen(value));
            ret[key] = wvalue;
        }
    }

    return ret;
}

void CDatabaseManager::InitPython(PyObject* poSelf, PyObject* poEngine)
{
    m_ppyDatabase = poSelf;
    PyCallClassMemberFunc(poSelf, "CreateSchema", Py_BuildValue("(O)", poEngine));
}
