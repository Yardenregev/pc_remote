from django.http import JsonResponse
from django.shortcuts import render
from .models import Keyboard, Mouse, VolumeController
import json

keyboard = Keyboard()
mouse = Mouse()
volume_controller = VolumeController()

def index(request):
    return render(request, 'control/home.html', {'keyboard': keyboard, 'volume': volume_controller.get_volume()})

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

def click_mouse(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        button = body.get('button','left')
        try:
            mouse.click_mouse(button)
            return JsonResponse({'status': 'success', 'message': f'clicked button {button}'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def scroll(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        value = body.get('value',0)
        print(f'{value=}')
        mouse.scroll(value)
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def set_volume(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        level = body.get('level',0)
        print(f'{level=}')
        volume_controller.set_volume(level)
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})