#pragma once
#include <map>
#include <string>
#include <vector>

class CDatabaseManager : public singleton<CDatabaseManager>
{
public:
    CDatabaseManager();
    virtual ~CDatabaseManager();

    void InitPython(PyObject* poSelf);

    std::map<int, std::wstring> Execute(std::wstring& query);

public:
    PyObject* m_ppyDatabase;
    bool bPythonInit;
};
