#https://www.youtube.com/watch?v=D8-snVfekto
#https://github.com/teacherRay/weather_app

import requests
import tkinter as tk

LIGHTBLUE = "#03bafc"
DARKBLUE = "#034efc"
PALEBLUE = "#c1f0f5"

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = LIGHTBLUE)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

button = tk.Button(frame, text = "Test Button", bg = DARKBLUE, fg = PALEBLUE)
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25, anchor="nw")

label = tk.Label(frame, text = "My Label", bg = DARKBLUE, fg = PALEBLUE)
label.place(relx=0.26, rely=0, relwidth=0.25, relheight=0.25)

entry = tk.Entry(frame, bg = DARKBLUE, fg = PALEBLUE)
entry.place(relx=0.52, rely=0, relwidth=0.475, relheight=0.25)

root.mainloop()