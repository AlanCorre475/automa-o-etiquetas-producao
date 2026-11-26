@echo off
REM Arraste o PDF das ordens de producao em cima deste arquivo
if "%~1"=="" (
    echo Arraste o PDF das ordens de producao em cima deste arquivo.
    pause
    exit /b
)
python "%~dp0extrair_etiquetas.py" "%~1"
pause
