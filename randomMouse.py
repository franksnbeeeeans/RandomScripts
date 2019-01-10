from pynput.keyboard import Listener
from pynput.mouse import Controller
import random
import time


validity = True
def on_press(key):
    if str(key) == 'Key.enter':
        global validity
        validity = False
    else:
        pass


def controlMouse():
    mouse = Controller()
    keyboard = Listener()
    print("Press Enter to exit")
    while True:
        mouse.move(random.randint(0,10), random.randint(0,10))
        with Listener(on_press=on_press) as listener:
            if not validity:
                raise SystemExit
            time.sleep(1)


controlMouse()
