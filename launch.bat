@echo off
call C:\Users\yardi\OneDrive\Desktop\Yarden\Code\remote_pc_trackpad\env\Scripts\activate.bat
cd C:\Users\yardi\OneDrive\Desktop\Yarden\Code\remote_pc_trackpad\pc_remote
python manage.py runserver_plus --cert-file selftest-cert.crt 0.0.0.0:8443
pause