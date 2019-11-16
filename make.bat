@echo off

if "%1" == "" ( echo  build - Gera o build da aplicação)
if "%1" == "build" (
	py setup.py sdist bdist_wheel
	goto :EOF
)

if "%1" == "" ( echo install - Instala a aplicação)
if "%1" == "install" (
	pip install .
	goto :EOF
)

if "%1" == "" ( echo test - Executa a suíte de testes)
if "%1" == "test" (
	python setup.py test
	goto :EOF
)

