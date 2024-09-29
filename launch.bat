@echo off
call C:\Users\yardi\OneDrive\Desktop\Yarden\Code\remote_pc_trackpad\env\Scripts\activate.bat
cd C:\Users\yardi\OneDrive\Desktop\Yarden\Code\remote_pc_trackpad\pc_remote
python manage.py runserver_plus --key-file selftest-key --cert-file selftest-cert 0.0.0.0:8443
pause