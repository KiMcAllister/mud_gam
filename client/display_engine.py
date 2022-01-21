import threading
import time
import msvcrt
import client
from ctypes import *

kernel32 = windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

updated = True

class myThread (threading.Thread):
    def __init__(self):
      threading.Thread.__init__(self)
      self.current = []
    def run(self):
        while True:
            if msvcrt.kbhit():
                global updated
                user_i = msvcrt.getwche()
                if user_i == '\x00':
                    self.current.append(user_i + msvcrt.getwche())
                elif user_i == '\r':
                    client.send_input(''.join(user_input.current))
                    self.current.clear()
                else:
                    self.current.append(user_i)

# Create user input thread
user_input = myThread()

# Start user input thread
user_input.start()

# some variables just to test printing and recieving use input at the same time
current_text = "Type something:"
back = "\033[1D"

#main loop
while True:
    text = client.get_text()
    if not text:
        pass
    else: 
        updated = True
        current_text = text
    
    if updated:
        print(f"\r{str(current_text)}\n>", end = '')
        updated = False
    else:
        print("\r> {}".format(''.join(user_input.current)), end = '')