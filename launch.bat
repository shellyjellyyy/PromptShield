@echo off
title PromptShield Launcher
color 0A

echo ===================================================
echo           PROMPTSHIELD SECURITY SUITE
echo ===================================================
echo.

:: Move to the folder where this script is located
cd /d "%~dp0"

echo Current Directory: %CD%
echo Starting PromptShield React Dashboard...
echo.

:: Launch the app server
python code/app.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Failed to start with python command. Trying py launcher...
    py code/app.py
)

pause
