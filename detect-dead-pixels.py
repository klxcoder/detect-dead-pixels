#!/usr/bin/python

import random
import tkinter as tk
import threading
import time
import signal, os, sys

def handler(signum, frame):
  signame = signal.Signals(signum).name
  if signame == "SIGINT":
    print("Goodbye")
    sys.exit(0)

def random_color():
  str = '#'
  for i in range(6):
    str = str + random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'])
  return str

win = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

win.attributes('-fullscreen', True)

win.configure(bg=random_color())

def change_bg():
  while True:
    win.configure(bg=random_color())
    time.sleep(1)

threading.Thread(target=change_bg, daemon=True).start()

signal.signal(signal.SIGINT, handler)
print("Press Ctr+C to stop")
win.mainloop()
