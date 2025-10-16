@echo off
setlocal
set SCRIPT_DIR=%~dp0
cd /d %SCRIPT_DIR%
if not exist .venv (
    py -m venv .venv
)
call .venv\Scripts\activate
pip install -r requirements.txt >nul 2>&1
py build.py --platform windows
echo Built to dist\windows\Foxyiz.exe
endlocal
