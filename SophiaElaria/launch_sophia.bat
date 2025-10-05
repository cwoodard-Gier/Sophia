@echo off
REM Activate conda environment and run Sophia assistant

CALL C:\Users\cwood\miniconda3\Scripts\activate.bat sophia
cd /d "C:\Users\cwood\OneDrive\Desktop\SophiaElaria"
python sophiaassistant.py

REM This keeps the window open so you see all output/errors
echo.
echo Press any key to exit...
pause >nul