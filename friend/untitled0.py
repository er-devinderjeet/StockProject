# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:41:58 2017

@author: Devinderjeet
"""

	
from Tkinter import *

root = Tk()

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    print "clicked at", event.x, event.y

canvas= Canvas(root, width=100, height=100)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()

root.mainloop()