rem Requires:
rem * pyinstaller 5.0.dev0 for build
rem * matplotlib 3.5.1
pyinstaller --noconsole --noconfirm --clean main.py
set program-name=wifi-strength


rem pyinstaller creates a build directory - comment this if you need it
if exist "build" rmdir /s /q build

rem Renames the main (from main.py) to program name
move /y .\dist\main .\dist\%program-name%

rem Move into the dist folder
rem old command to make tarball, new command to make 7z zip file
REM cd dist
REM tar -czf  %program-name%.tar.gz %program-name%
REM cd..
REM move /y .\dist\%program-name%.tar.gz .\%program-name%.tar.gz
7z a -tzip %program-name%.zip .\dist\%program-name%

rem Cleanup and remove dist folder - comment this if you need it
rmdir /s /q dist