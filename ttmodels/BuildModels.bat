@echo off
echo Waiting 5 seconds before running panda premake...
timeout 5
ppremake.exe
echo . . . .
echo - - - -
echo . . . .
timeout 5
make install
pause