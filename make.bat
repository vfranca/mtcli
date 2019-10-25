@echo off

if "%1" == "" ( echo build)
if "%1" == "build" (
	py setup.py sdist bdist_wheel
	goto :EOF
)

if "%1" == "" ( echo install)
if "%1" == "install" (
	pip install --upgrade dist/cli_trade-0.1.tar.gz
	goto :EOF
)

if "%1" == "" ( echo test)
if "%1" == "test" (
	py -m unittest %2
	rem goto :EOF
)

