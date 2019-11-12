#https://www.youtube.com/watch?v=D8-snVfekto
#https://github.com/teacherRay/weather_app

#463b0ae259c10982f0e5d0dccf54bde5

import requests
import tkinter as tk

LIGHTBLUE = "#03bafc"
DARKBLUE = "#034efc"
PALEBLUE = "#c1f0f5"

HEIGHT = 500
WIDTH = 600


def format_response(weather):
   try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature °C: %s '% (name, desc, temp)
        

   except:
        final_str = "There was a problem retrieving that information."
   return final_str



def get_weather(city):
    weather_key = '463b0ae259c10982f0e5d0dccf54bde5'   
    url ='https://api.openweathermap.org/data/2.5/weather' 
    params = {'APPID': weather_key,'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    

    label['text'] = format_response(weather)

root = tk.Tk()

canvas=tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file ='landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)
frame = tk.Frame(root, bg = DARKBLUE, bd = 3)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = 40)
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", command = lambda:get_weather(entry.get()))
button.place(relx =.67,rely = 0, relwidth = 0.32, relheight = 1)

lower_frame = tk.Frame(root, bg = DARKBLUE,bd = 3)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, font = ('Courier', 18))
label.place(relwidth = 1, relheight = 1)

root.mainloop()