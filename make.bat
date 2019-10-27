@echo off

if "%1" == "-h" ( echo "" - Build para wheel)
if "%1" == "" (
	py setup.py sdist bdist_wheel
	goto :EOF
)

if "%1" == "-h" ( echo install - Instala)
if "%1" == "install" (
	pip install .
	goto :EOF
)

if "%1" == "-h" ( echo test - Executa a suíte de testes)
if "%1" == "test" (
	py -m unittest %2
	goto :EOF
)

