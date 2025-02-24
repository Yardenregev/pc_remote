"""
WSGI config for pc_remote project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from socket import gethostname
from colorama import init as colorama_init
from colorama import Fore, Style
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pc_remote.settings')

application = get_wsgi_application()

colorama_init()
host = gethostname()
print(f"{Fore.GREEN}Access the platform on {Fore.CYAN}https://{host}:8443 {Fore.GREEN}or {Fore.CYAN}https://{host}.local:8443{Style.RESET_ALL}")
