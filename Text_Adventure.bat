@echo off
cd /d "%~dp0" 2>nul || (
    echo  [ERROR] Cannot access script directory.
    pause & exit /b 1
)
REM This batch file provides a menu-driven interface for the Text Adventure Game.

:menu
cls
echo ================================================================================
echo     Jules' Text Adventure Game - Main Menu
echo ================================================================================
echo.
echo Please choose an option:
echo.
echo   1) Run Jules-Experiment
echo   2) Validate Installation
echo   3) Install Requirements
echo   4) Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto run_game
if "%choice%"=="2" goto validate_install
if "%choice%"=="3" goto install_reqs
if "%choice%"=="4" goto exit_script

echo Invalid choice. Please try again.
pause
goto menu

:run_game
echo "Starting Text Adventure Game..."
python launcher.py
echo.
echo "Game has exited. Press any key to return to the menu."
pause > nul
goto menu

:validate_install
python validater.py
echo.
echo "Validation complete. Press any key to return to the menu."
pause > nul
goto menu

:install_reqs
python installer.py
echo.
echo "Installation process complete. Press any key to return to the menu."
pause > nul
goto menu

:exit_script
exit