@echo off
REM Activate the sophia environment
CALL "%USERPROFILE%\miniconda3\Scripts\activate.bat" sophia
REM Change directory to project
cd /d "%USERPROFILE%\OneDrive\Desktop\SophiaElaria"
REM Install all required pip packages from requirements.txt
pip install --upgrade pip
pip install -r requirements.txt
echo.
echo All requirements installed!
echo Press any key to exit...
pause >nul