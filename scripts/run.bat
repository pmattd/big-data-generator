@ECHO OFF
ECHO Launching data generator

set PYTHONPATH=%PYTHONPATH%;%CD%\..

python ..\data_generator\app.py --verbose
