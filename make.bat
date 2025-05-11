@echo off
set version=1.9.1
set dist=mtcli

if /i "%1" == "build" (
goto :build
)
if /i "%1" == "publish" (
goto :publish
) else (
echo escolha build ou publish
goto :eof
)

:build
set mtcli=Mtcli.ex5
set ma_txt=MA_TXT.ex5
set readme=readme.md
set license=LICENSE
set buildpath=build\
set distpath=dist\pyinstaller\mtcli-%version%\
set fzip=mtcli-%version%.zip
pyinstaller --distpath dist/pyinstaller -y mt.spec
copy %buildpath%%mtcli% %distpath%%mtcli%
copy %buildpath%%ma_txt% %distpath%%ma_txt%
copy docs\%readme% %distpath%%readme%
copy %license% %distpath%%license%
cd %distpath%
call zip -r %fzip% *.*
move %fzip% ..\%fzip%
cd ..\..\..
rd /s /q %distpath%
goto :eof

:publish
set distpath="C:\Users\Administrador\cli\mtcli\dist\pyinstaller"
set drive="G:\Meu Drive"
set mtcliws="C:\Users\Administrador\cli\mtcli-ws\mtcli-ws\BIN"
copy %distpath%\%dist%-%version%.zip %mtcliws%\%dist%.zip
copy %distpath%\%dist%-%version%.zip %drive%\%dist%.zip
copy %distpath%\%dist%-%version%.zip %drive%\%dist%-%version%.zip
goto :eof
