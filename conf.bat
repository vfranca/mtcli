@echo off
if not "%1" == "" (
dotenv -f .mtcli set %1 %2
goto :EOF
)
dotenv -f .mtcli list
