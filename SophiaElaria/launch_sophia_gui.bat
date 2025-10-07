@echo off
REM One-click launcher for SophiaElaria GUI

CALL "%USERPROFILE%\miniconda3\Scripts\activate.bat" sophia
cd /d "%USERPROFILE%\OneDrive\Desktop\SophiaElaria"
python sophia_gui.py

echo.
echo GUI session ended. Press any key to exit...
pause >nul