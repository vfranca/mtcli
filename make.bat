@echo off

rem Exibe todas as tarefas
if "%1" == "" (
echo build
echo pos-release
echo deploy
echo check
goto :EOF
)

rem Executa o build
if "%1" == "build" (
call :build
goto :EOF
)

rem Executa o pos-release
if "%1" == "pos-release" (
call :pos-release
goto :EOF
)

rem Executa o deploy
if "%1" == "deploy" (
call :deploy
goto :EOF
)

rem Executa a checagem
if "%1" == "check" (
call :check
goto :EOF
)

:build
echo executando black
black mtcli
black tests
echo executando testes
pytest -q
echo executando build
poetry build
echo instalando local
poetry install
echo fim
goto :EOF

:pos-release
echo executando pos-release
git push
git push --tags
git push origin master
goto :EOF

:deploy
echo executando black
black mtcli
black tests
echo executando tests
pytest -q
echo executando o build
poetry build
echo executando o deploy
poetry publish
echo fim
goto :EOF

:check
echo executando checagem
echo verificando testes
pytest -q
echo verificando codificacao
black mtcli tests
echo verificando poetry
poetry check
echo verificando status do repositorio local
git status
echo fim
goto :EOF
