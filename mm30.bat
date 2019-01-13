@echo off
set f="wing19m30.csv"
set mm="sma"
py %mm%.py 17 %f%
py %mm%.py 34 %f%
py %mm%.py 72 %f%
