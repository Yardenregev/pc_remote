from django.http import JsonResponse
from django.shortcuts import render
from .models import Keyboard
import json

keyboard = Keyboard()  # Initialize the keyboard object

def index(request):
    return render(request, 'control/home.html', {'keyboard': keyboard})

def keypress(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        key = body.get('key')
        if key:
            keyboard.press_key(key)
            return JsonResponse({'status': f'pressed {key}'})
    return JsonResponse({'status': 'Invalid request'}, status=400)
