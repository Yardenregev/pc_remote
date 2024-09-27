# keyboard/models.py
from pynput.keyboard import Controller , Key
class MyKey:
    
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
            MyKey('1', '1', 1, 1), MyKey('2', '2', 1, 2), MyKey('3', '3', 1, 3), MyKey('4', '4', 1, 4), 
            MyKey('5', '5', 1, 5), MyKey('6', '6', 1, 6), MyKey('7', '7', 1, 7), MyKey('8', '8', 1, 8), 
            MyKey('9', '9', 1, 9), MyKey('0', '0', 1, 10),
            MyKey('<---', 'backspace', 1, 11, width=2),  # Backspace with extra width

            # Second row (QWERTY)
            MyKey('Q', 'q', 2, 1), MyKey('W', 'w', 2, 2), MyKey('E', 'e', 2, 3), MyKey('R', 'r', 2, 4), 
            MyKey('T', 't', 2, 5), MyKey('Y', 'y', 2, 6), MyKey('U', 'u', 2, 7), MyKey('I', 'i', 2, 8), 
            MyKey('O', 'o', 2, 9), MyKey('P', 'p', 2, 10),
            MyKey('Delete', 'delete', 2, 11),

            # Third row (ASDF)
            MyKey('A', 'a', 3, 1), MyKey('S', 's', 3, 2), MyKey('D', 'd', 3, 3), MyKey('F', 'f', 3, 4), 
            MyKey('G', 'g', 3, 5), MyKey('H', 'h', 3, 6), MyKey('J', 'j', 3, 7), MyKey('K', 'k', 3, 8), 
            MyKey('L', 'l', 3, 9), MyKey('Enter', 'enter', 3, 10, width=2),  # Enter key with extra width

            # Fourth row (ZXCV)
            MyKey('Z', 'z', 4, 1), MyKey('X', 'x', 4, 2), MyKey('C', 'c', 4, 3), MyKey('V', 'v', 4, 4), 
            MyKey('B', 'b', 4, 5), MyKey('N', 'n', 4, 6), MyKey('M', 'm', 4, 7), 

            # Fifth row (spacebar and special keys)
            MyKey('Space', 'space', 5, 3, width=5),  # Space bar across 5 columns
            MyKey('←', 'left', 5, 9),  # Left arrow
            MyKey('→', 'right', 5, 10),  # Right arrow
            MyKey('↑', 'up', 4, 9),  # Up arrow
            MyKey('↓', 'down', 5, 7),  # Down arrow
        ]
        self.controller = Controller()
    
    def press_key(self, key):
        # Simulate the key press
        if key in self.special_keys_map:
            key = self.special_keys_map[key]
        self.controller.tap(key)
