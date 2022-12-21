@echo off
if not "%1" == "" (
dotenv set %1 %2
goto :EOF
)
dotenv list
