# -*- coding: utf-8 -*-

#测试doc_string
import odbchelper

params = {"server": "mpilgrimtest", "database": "mastertest", "uid": "satest", "pwd": "secrettest"}
print odbchelper.buildConnectionString(params)
print odbchelper.buildConnectionString.__doc__
