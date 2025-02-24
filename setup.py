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
from colors import GREEN, RED, YELLOW, CYAN, COLOR_RESET

def create_venv():
    print("\nCreating virtual environment...")
    venv_path = Path("venv")
    venv.create(venv_path, with_pip=True)
    
    pip_path = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / "pip"
    return pip_path, venv_path

def install_requirements(pip_path):
    print("\nInstalling requirements...")
    subprocess.check_call([str(pip_path), "install", "-r", "requirements.txt"])

def create_env_file():
    print("\nCreating .env file...")
    print(f"{YELLOW}Please visit {CYAN}https://djecrety.ir/ {YELLOW}to generate a secure Django secret key{COLOR_RESET}")
    secret_key = input(GREEN+"Enter your secret key: "+COLOR_RESET)
    
    env_path = Path("pc_remote") / ".env"
    env_path.write_text(f'SECRET_KEY="{secret_key}"\n')

def create_superuser(venv_path):
    print("\nCreating superuser...")
    username = input(GREEN+"Enter superuser username: "+COLOR_RESET)
    email = input(GREEN+"Enter superuser email: "+COLOR_RESET)
    password = getpass(GREEN+"Enter superuser password: "+COLOR_RESET)
    confirm_password = getpass(GREEN+"Confirm password: "+COLOR_RESET)
    while password != confirm_password:
        print(RED+"Passwords don't match!"+COLOR_RESET)
        password = getpass(GREEN+"Enter superuser password: "+COLOR_RESET)
        confirm_password = getpass(GREEN+"Confirm password: "+COLOR_RESET)
    
    command = f"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('{username}', '{email}', '{password}')"
    python_path = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / "python"
    subprocess.check_call([str(python_path), Path("pc_remote/manage.py"), "shell", "-c", command])

def generate_ssl_cert():
    print("\nGenerating SSL certificate...")
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, u"pc_remote")])
    cert = (x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(private_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
            .not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365))
            .sign(private_key, hashes.SHA256()))
    
    cert_path = Path("pc_remote")
    cert_path.mkdir(parents=True, exist_ok=True)
    (cert_path / "certificate.crt").write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    (cert_path / "private.key").write_bytes(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

def run_migrations(venv_path):
    print("\nRunning migrations...")
    python_path = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / "python"
    subprocess.check_call([str(python_path), Path("pc_remote/manage.py"), "migrate"])

def main():
    print("Setting up your project...")
    pip_path, venv_path = create_venv()
    install_requirements(pip_path)
    create_env_file()
    generate_ssl_cert()
    run_migrations(venv_path)
    create_superuser(venv_path)
    print(GREEN+"\n=== SETUP COMPLETE ==="+COLOR_RESET)

if __name__ == "__main__":
    main()
