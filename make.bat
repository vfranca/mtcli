@echo off
set version=2.0.0
set dist=mtcli
set cmd=%1

if /i "%cmd%" == "test" (
	goto :test
)

if /i "%cmd%" == "format" (
	goto :format
)

if /i "%cmd%" == "build" (
	goto :build
)

if /i "%cmd%" == "publish" (
	goto :publish
)

echo Comando invalido: %cmd%
echo Uso: make [test] [format] [build] [publish]
goto :eof

:test
echo Executando testes...
poetry run pytest
goto :EOF

:format
echo Formatando o codigo com black...
poetry run black mtcli tests
goto :EOF

:build
echo Executando build com pyinstaller...
set mtcli=Mtcli.ex5
set ma_txt=MA_TXT.ex5
set readme=readme.md
set license=LICENSE
set buildpath=build\
set distpath=dist\pyinstaller\mtcli-%version%\
set fzip=mtcli-%version%.zip
poetry run pyinstaller --distpath dist/pyinstaller -y mt.spec
copy %buildpath%%mtcli% %distpath%%mtcli%
rem copy %buildpath%%ma_txt% %distpath%%ma_txt%
copy docs\%readme% %distpath%%readme%
copy %license% %distpath%%license%
cd %distpath%
call zip -r %fzip% *.*
move %fzip% ..\%fzip%
cd ..\..\..
rd /s /q %distpath%
goto :eof

:publish
echo Publicando o portável no google drive...
set distpath="C:\Users\Administrador\cli\mtcli\dist\pyinstaller"
set drive="G:\Meu Drive"
set mtcliws="C:\Users\Administrador\cli\mtcli-ws\mtcli-ws\BIN"
copy %distpath%\%dist%-%version%.zip %mtcliws%\%dist%.zip
copy %distpath%\%dist%-%version%.zip %drive%\%dist%.zip
copy %distpath%\%dist%-%version%.zip %drive%\%dist%-%version%.zip
goto :eof
