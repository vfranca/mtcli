@echo off
py reader.py %WDO%m30.csv 1
py reader.py %WDO%h1.csv 1
py reader.py wdo@daily.csv 1
time /t
