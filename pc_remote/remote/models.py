# keyboard/models.py
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button as MouseButton
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

class KeyboardKey:
    
    def __init__(self, label, value, row, col, width=1, empty_space=False):
        self.label = label        # The label on the key (e.g., 'A', 'Enter', '→')
        self.value = value        # The actual character or control it represents
        self.row = row            # Row position for rendering
        self.col = col            # Column position for rendering
        self.width = width        # Width of the key (to accommodate larger keys like "Enter")
        self.empty_space = empty_space
    
class Keyboard:
    def __init__(self):
        
        self.special_keys_map = {
        "backspace": Key.backspace,
        "tab": Key.tab,
        "enter": Key.enter,
        "space": Key.space,
        "delete": Key.delete,
        "up": Key.up,
        "down": Key.down,
        "left": Key.left,
        "right": Key.right
        }
        self.arrow_keys = [
            KeyboardKey('','',1,1,empty_space=True),
            KeyboardKey('↑', 'up', 1, 2),  # Up arrow
            KeyboardKey('','',1,3,empty_space=True),
            KeyboardKey('←', 'left', 2, 1),  # Left arrow
            KeyboardKey('↓', 'down', 2, 2),  # Down arrow
            KeyboardKey('→', 'right', 2, 3),  # Right arrow
        ]
        self.special_keys = [
            KeyboardKey('Backspace', 'backspace', 1, 1),
            KeyboardKey('Delete', 'delete', 2, 1),
            KeyboardKey('Enter', 'enter', 3, 1),
        ]
    
        self.controller = KeyboardController()
    
    def press_key(self, key):

        if key in self.special_keys_map:
            key = self.special_keys_map[key]
        self.controller.tap(key)

    def type_input(self, message):
        self.controller.type(message)
        
class Mouse:
    def __init__(self):
        self.controller = MouseController()
    
    def move_mouse(self, x, y):
        
        # Move the mouse relative to its current position
        current_x, current_y = self.controller.position
        self.controller.position = (current_x + x, current_y + y)
    
    def click_mouse(self, button="left"):
        if button == "left":
            self.controller.click(MouseButton.left)
        elif button == "right":
            self.controller.click(MouseButton.right)
        else:
            raise ValueError("Invalid button specified. Must be one of 'left' or 'right'.")
    def scroll(self,value):
        step = 0
        if 0 <= value < 50:
            step = 1
        elif 50 < value <= 100:
            step = -1
        self.controller.scroll(0, step)
class VolumeController:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        
    def set_volume(self, level):
        level = max(0, min(level, 100))  # Ensure the volume stays between 0 and 100
        self.volume.SetMasterVolumeLevelScalar(level / 100, None)

    def get_volume(self):
        volume = int(self.volume.GetMasterVolumeLevelScalar() * 100)
        return volume