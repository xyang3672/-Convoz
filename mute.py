from pynput.keyboard import Key, Controller

def controlKeyboard():
    keyboard = Controller()
    with keyboard.pressed(Key.alt):
        keyboard.press('a')
        keyboard.release('a')

controlKeyboard()
