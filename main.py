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

frame = tk.Frame(root, bg = DARKBLUE,bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor = 'n')

entry = tk.Entry(frame, font = 40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text = "Get Weather", bg = PALEBLUE, font = 30)
button.place(relx=.67,rely=0, relwidth=0.32, relheight=1)

lower_frame = tk.Frame(root, bg = DARKBLUE,bd=8)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor = 'n')

label = tk.Label(lower_frame, font = 40)
label.place(relwidth=1, relheight=1)

root.mainloop()