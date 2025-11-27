@echo off
echo Building Student Result Management System...
echo.

echo Cleaning previous builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo Installing dependencies...
pip install -r requirements.txt

echo Building dashboard executable...
pyinstaller dashboard.spec

echo Building report executable...
pyinstaller report.spec

echo.
echo Build completed! Check the dist folder for executables.
echo.
pause
