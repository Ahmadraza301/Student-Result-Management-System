@echo off
title Student Result Management System Launcher
color 0A

echo.
echo ========================================
echo   Student Result Management System
echo ========================================
echo.
echo Choose an option:
echo.
echo 1. Launch Dashboard (Main Application)
echo 2. Launch Report Generator
echo 3. Exit
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo Launching Dashboard...
    start "" "dashboard.exe"
    goto :end
)

if "%choice%"=="2" (
    echo.
    echo Launching Report Generator...
    start "" "report.exe"
    goto :end
)

if "%choice%"=="3" (
    echo.
    echo Goodbye!
    goto :end
)

echo.
echo Invalid choice. Please try again.
pause
goto :menu

:end
echo.
echo Application launched successfully!
timeout /t 3 >nul
exit
