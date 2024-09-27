# keyboard/models.py
from pynput.keyboard import Controller

class Key:
    def __init__(self, label, value, row, col, width=1):
        self.label = label        # The label on the key (e.g., 'A', 'Enter', '→')
        self.value = value        # The actual character or control it represents
        self.row = row            # Row position for rendering
        self.col = col            # Column position for rendering
        self.width = width        # Width of the key (to accommodate larger keys like "Enter")

class Keyboard:
    def __init__(self):
        self.keys = [
            # First row (numbers and special characters)
            Key('1', '1', 1, 1), Key('2', '2', 1, 2), Key('3', '3', 1, 3), Key('4', '4', 1, 4), 
            Key('5', '5', 1, 5), Key('6', '6', 1, 6), Key('7', '7', 1, 7), Key('8', '8', 1, 8), 
            Key('9', '9', 1, 9), Key('0', '0', 1, 10),

            # Second row (QWERTY)
            Key('Q', 'q', 2, 1), Key('W', 'w', 2, 2), Key('E', 'e', 2, 3), Key('R', 'r', 2, 4), 
            Key('T', 't', 2, 5), Key('Y', 'y', 2, 6), Key('U', 'u', 2, 7), Key('I', 'i', 2, 8), 
            Key('O', 'o', 2, 9), Key('P', 'p', 2, 10),
            Key('Backspace', '\b', 2, 11, width=2),  # Backspace with extra width

            # Third row (ASDF)
            Key('A', 'a', 3, 1), Key('S', 's', 3, 2), Key('D', 'd', 3, 3), Key('F', 'f', 3, 4), 
            Key('G', 'g', 3, 5), Key('H', 'h', 3, 6), Key('J', 'j', 3, 7), Key('K', 'k', 3, 8), 
            Key('L', 'l', 3, 9), Key('Enter', 'enter', 3, 10, width=2),  # Enter key with extra width

            # Fourth row (ZXCV)
            Key('Z', 'z', 4, 1), Key('X', 'x', 4, 2), Key('C', 'c', 4, 3), Key('V', 'v', 4, 4), 
            Key('B', 'b', 4, 5), Key('N', 'n', 4, 6), Key('M', 'm', 4, 7), 

            # Fifth row (spacebar and special keys)
            Key('Space', 'space', 5, 3, width=5),  # Space bar across 5 columns
            Key('Delete', 'delete', 5, 8),
            # Key('←', 'left', 5, 9),  # Left arrow
            # Key('→', 'right', 5, 10),  # Right arrow
            # Key('↑', 'up', 4, 9),  # Up arrow
            # Key('↓', 'down', 5, 7),  # Down arrow
        ]
        self.controller = Controller()
    
    def press_key(self, key):
        if key.lower() == 'enter':
            key = '\n'
        elif key.lower() == 'space':
            key = ' '
        elif key.lower() == 'backspace':
            key = '\b'
        elif key.lower() == 'tab':
            key = '\t'
        elif key.lower() == 'delete':
            key = '\x08'
        elif key.lower() == 'escape':
            key = '\x1b'
        elif key.lower() == 'up':
            key = '\x1b[A'
        elif key.lower() == 'down':
            key = '\x1b[B'
        elif key.lower() == 'left':
            key = '\x1b[D'
        elif key.lower() == 'right':
            key = '\x1b[C'
        # Simulate the key press
        self.controller.press(key)
        self.controller.release(key)
        print("Pressed: " + key)
