@echo off
call env\Scripts\activate.bat
cd pc_remote
python manage.py runserver_plus --cert-file selftest-cert.crt 0.0.0.0:8443
pause