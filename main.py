#https://www.youtube.com/watch?v=D8-snVfekto
#https://github.com/teacherRay/weather_app

import requests
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

#def helloCallBack():
#       msg = messagebox.showinfo( "Hello Python", "Hello World")
canvas = tk.Canvas(root, height = 400, width = 600)
canvas.pack()

frame = tk.Frame(root, bg= "pink")
frame.place(relx = 0.1, rely = 0.1, relheight = 0.8, relwidth = 0.8)

button = tk.Button(root, text = "test button", bg = "red", fg = "yellow")
button.pack()

root.mainloop()