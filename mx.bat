@echo off
py reader.py %t%m5.csv 1
py reader.py %t%m15.csv 1
rem py reader.py %t%m30.csv 1
py reader.py %t%h1.csv 1
time /t
