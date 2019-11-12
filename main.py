#https://www.youtube.com/watch?v=D8-snVfekto
#https://github.com/teacherRay/weather_app

import requests
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

LIGHTBLUE = "#03bafc"
DARKBLUE = "#034efc"
PALEBLUE = "#c1f0f5"

#def helloCallBack():
#       msg = messagebox.showinfo( "Hello Python", "Hello World")
canvas = tk.Canvas(root, height = 400, width = 600)
canvas.pack()

frame = tk.Frame(root, bg = LIGHTBLUE)
frame.place(relx = 0.1, rely = 0.1, relheight = 0.8, relwidth = 0.8)

button = tk.Button(frame, text = "Test Button", bg = DARKBLUE, fg = PALEBLUE)
label = tk.Label(frame, text = "My lovely label", bg = DARKBLUE, fg = PALEBLUE)
entry = tk.Entry(frame, text = "My entry", bg = DARKBLUE, fg = PALEBLUE)

button.pack()
label.pack()
entry.pack()

root.mainloop()