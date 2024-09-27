from django.http import JsonResponse
from django.shortcuts import render
from .models import Keyboard, Mouse
import json

keyboard = Keyboard()  # Initialize the keyboard object
mouse = Mouse() # Initialize the mouse object
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

def input(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        message = body.get('input')
        if message:
            keyboard.type_input(message)
            return JsonResponse({'status': f'sent {message}'})
    return JsonResponse({'status': 'Invalid request'}, status=400)

def move_mouse(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        x = body.get('x',0)
        y = body.get('y',0)
    
        mouse.move_mouse(x, y)
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})