import os
import venv
import subprocess
import sys
from pathlib import Path
from getpass import getpass
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime
from colors import GREEN, RED,YELLOW, CYAN,COLOR_RESET

def create_venv():
    print("\nCreating virtual environment...")
    venv.create('venv', with_pip=True)
    
    # Determine the path to pip based on OS
    if sys.platform == 'win32':
        pip_path = 'venv\\Scripts\\pip'
        activate_path = 'venv\\Scripts\\activate'
    else:
        pip_path = 'venv/bin/pip'
        activate_path = 'venv/bin/activate'
    
    return pip_path, activate_path

def install_requirements(pip_path):
    print("\nInstalling requirements...")
    subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])

def create_env_file():
    print("\nCreating .env file...")
    print(f"{YELLOW}Please visit {CYAN}https://djecrety.ir/ {YELLOW}to generate a secure Django secret key{COLOR_RESET}")
    secret_key = input(GREEN+"Enter your secret key: "+COLOR_RESET)
    
    with open('pc_remote\\.env', 'w') as f:
        f.write(f'SECRET_KEY="{secret_key}"\n')

def create_superuser():
    print("\nCreating superuser...")
    username = input(GREEN+"Enter superuser username: "+COLOR_RESET)
    email = input(GREEN+"Enter superuser email: "+COLOR_RESET)
    password = getpass(GREEN+"Enter superuser password: "+COLOR_RESET)
    confirm_password = getpass(GREEN+"Confirm password: "+COLOR_RESET)
    while password != confirm_password:
        print(RED+"Passwords don't match!"+COLOR_RESET)
        password = getpass(GREEN+"Enter superuser password: "+COLOR_RESET)
        confirm_password = getpass(GREEN+"Confirm password: "+COLOR_RESET)
    
    # Create the command to run with manage.py
    command = f"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('{username}', '{email}', '{password}')"
    
    if sys.platform == 'win32':
        python_path = 'venv\\Scripts\\python'
    else:
        python_path = 'venv/bin/python'
    
    subprocess.check_call([python_path, 'pc_remote\\manage.py', 'shell', '-c', command])

def generate_ssl_cert():
    print("\nGenerating SSL certificate...")
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Create certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, u"pc_remote"),
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.now(datetime.timezone.utc)
    ).not_valid_after(
        datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365)
    ).sign(private_key, hashes.SHA256())

    # Save files
    with open("pc_remote\\certificate.crt", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    with open("pc_remote\\private.key", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

def run_migrations():
    print("\nRunning migrations...")
    
    if sys.platform == 'win32':
        python_path = 'venv\\Scripts\\python'
    else:
        python_path = 'venv/bin/python'
    
    subprocess.check_call([python_path, 'pc_remote\\manage.py', 'migrate'])

def main():
    print("Setting up your project...")
    
    pip_path, _ = create_venv()
    
    install_requirements(pip_path)
    
    create_env_file()
    
    generate_ssl_cert()
    
    run_migrations()
    
    # Create superuser
    create_superuser()
    
    print(GREEN+"\n=== SETUP COMPLETE ==="+COLOR_RESET)

if __name__ == "__main__":
    main()