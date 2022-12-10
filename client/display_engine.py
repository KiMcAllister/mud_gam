import threading
import msvcrt
import client
from ctypes import *
import os


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
                elif user_i == '\x08':
                    try:
                        self.current.append("\033[F")
                        #del self.current[-1]
                    except IndexError:
                        self.current = self.current
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
    os.get_terminal_size()[0]
    if updated:
        print(f"\r{str(current_text)}\n>", end = '')
        updated = False
    else:
        if (len(user_input.current) > os.get_terminal_size()[0]):
            print("\r> {}".format(''.join(user_input.current)), end = '')
        else:
            print("\r> {}".format(''.join(user_input.current)), end = '')