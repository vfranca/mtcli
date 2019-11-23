@echo off

if "%1" == "" (
call :task clean
call :task test
call :task build
call :task deploy
call :task install
)

:task
if "%1" == "clean" (
rm -rf build
rm -rf dist
rm -rf chartcli.egg-info
)
if "%1" == "test" (
python setup.py test
)
if "%1" == "build" (
py setup.py sdist bdist_wheel
)
if "%1" == "deploy" (
twine upload dist/* --config-file .pypirc --repository testpypi
)
if "%1" == "install" (
pip install --upgrade -i https://test.pypi.org/simple/ chartcli
)
