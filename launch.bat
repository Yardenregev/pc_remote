@echo off
call env\Scripts\activate.bat
cd pc_remote
python manage.py runsslserver --certificate certificate.crt --key private.key 0.0.0.0:8443
pause