@echo off
CALL "%USERPROFILE%\miniconda3\Scripts\activate.bat" sophia
cd /d "%USERPROFILE%\OneDrive\Desktop\SophiaElaria"

echo What do you want to launch?
echo [1] Main Sophia Assistant (Voice)
echo [2] Sophia GUI (Chat)
set /p userchoice=Choice (1 or 2):

if "%userchoice%"=="1" (
    python sophiaassistant.py
) else (
    python sophia_gui.py
)

echo.
echo Session ended. Press any key to exit...
pause >nul