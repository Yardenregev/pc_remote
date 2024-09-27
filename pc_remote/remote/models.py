# keyboard/models.py
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button as MouseButton

class KeyboardKey:
    
    def __init__(self, label, value, row, col, width=1):
        self.label = label        # The label on the key (e.g., 'A', 'Enter', '→')
        self.value = value        # The actual character or control it represents
        self.row = row            # Row position for rendering
        self.col = col            # Column position for rendering
        self.width = width        # Width of the key (to accommodate larger keys like "Enter")
    
    
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
        
        self.keys = [
            # First row (numbers and special characters)
            KeyboardKey('1', '1', 1, 1), KeyboardKey('2', '2', 1, 2), KeyboardKey('3', '3', 1, 3), KeyboardKey('4', '4', 1, 4), 
            KeyboardKey('5', '5', 1, 5), KeyboardKey('6', '6', 1, 6), KeyboardKey('7', '7', 1, 7), KeyboardKey('8', '8', 1, 8), 
            KeyboardKey('9', '9', 1, 9), KeyboardKey('0', '0', 1, 10),
            KeyboardKey('<---', 'backspace', 1, 11, width=2),  # Backspace with extra width

            # Second row (QWERTY)
            KeyboardKey('Tab', 'tab', 2, 0, width=2),
            KeyboardKey('Q', 'q', 2, 1), KeyboardKey('W', 'w', 2, 2), KeyboardKey('E', 'e', 2, 3), KeyboardKey('R', 'r', 2, 4), 
            KeyboardKey('T', 't', 2, 5), KeyboardKey('Y', 'y', 2, 6), KeyboardKey('U', 'u', 2, 7), KeyboardKey('I', 'i', 2, 8), 
            KeyboardKey('O', 'o', 2, 9), KeyboardKey('P', 'p', 2, 10),
            KeyboardKey('Delete', 'delete', 2, 11),

            # Third row (ASDF)
            KeyboardKey('Caps Lock', 'caps_lock', 3, 0, width=2),
            KeyboardKey('A', 'a', 3, 1), KeyboardKey('S', 's', 3, 2), KeyboardKey('D', 'd', 3, 3), KeyboardKey('F', 'f', 3, 4), 
            KeyboardKey('G', 'g', 3, 5), KeyboardKey('H', 'h', 3, 6), KeyboardKey('J', 'j', 3, 7), KeyboardKey('K', 'k', 3, 8), 
            KeyboardKey('L', 'l', 3, 9), KeyboardKey('Enter', 'enter', 3, 10, width=2),  # Enter key with extra width

            # Fourth row (ZXCV)
            KeyboardKey('Z', 'z', 4, 1), KeyboardKey('X', 'x', 4, 2), KeyboardKey('C', 'c', 4, 3), KeyboardKey('V', 'v', 4, 4), 
            KeyboardKey('B', 'b', 4, 5), KeyboardKey('N', 'n', 4, 6), KeyboardKey('M', 'm', 4, 7), 

            # Fifth row (spacebar and special keys)
            KeyboardKey('Space', 'space', 5, 3, width=5),  # Space bar across 5 columns
            KeyboardKey('←', 'left', 5, 9),  # Left arrow
            KeyboardKey('→', 'right', 5, 10),  # Right arrow
            KeyboardKey('↑', 'up', 4, 9),  # Up arrow
            KeyboardKey('↓', 'down', 5, 7),  # Down arrow
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
