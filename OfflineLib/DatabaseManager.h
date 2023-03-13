#pragma once
#include <map>
#include <string>
#include <vector>

class CDatabaseManager : public singleton<CDatabaseManager>
{
public:
    CDatabaseManager();
    virtual ~CDatabaseManager();

    void InitPython(PyObject* poSelf, PyObject* poEngine, PyObject* poPhaseManager);

    std::map<int, std::wstring> Execute(std::wstring& query);

public:

    PyObject* m_ppyDatabase;
    PyObject* m_ppyPhaseManager;
    PyObject* m_ppyEngine;
    PyObject* GetEngine() { return m_ppyEngine; }
    PyObject* GetPhaseManager() { return m_ppyPhaseManager; }

    bool bPythonInit;
};
