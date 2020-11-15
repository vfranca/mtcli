@echo off
cls
if "%1" == "" (
pytest -q
goto :EOF
)
pytest -q tests/%1.py
