@set version=1.5.2
@set mtcli=Mtcli.ex5
@set ma_txt=MA_TXT.ex5
@set readme=readme.md
@set license=LICENSE
@set dir_build=build\
@set dir_dist=dist\pyinstaller\mtcli-%version%\
@pyinstaller --distpath dist/pyinstaller -y mt.spec
copy %dir_build%%mtcli% %dir_dist%%mtcli%
copy %dir_build%%ma_txt% %dir_dist%%ma_txt%
copy docs\%readme% %dir_dist%%readme%
copy %license% %dir_dist%%license%


set fzip=mtcli-%version%.zip
cd %dir_dist%
call zip -r %fzip% *.*
move %fzip% ..\%fzip%
cd ..\..\..
rd /s /q %dir_dist%
