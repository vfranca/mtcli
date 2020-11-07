@echo off

if "%1" == "" (
pytest -q
goto :EOF
)

pytest -q tests/test_%1.py
