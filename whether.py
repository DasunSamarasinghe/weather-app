from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk ,messagebox
from timezonefinder import timezonefinder
from datetime import datetime
import requests
import pytz


root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


#search box
search_image=PhotoImage(file="c:/Users/dasun/OneDrive/Desktop/wheather app/weather-app/search.png")
myimage=Label(image=search_image)
myimage.place(x=50,y=20)

Textfield=Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#fafafa",border=0,fg="black")
                
Textfield.place(x=50,y=40)
Textfield.focus()

search_icon=PhotoImage(file="c:/Users/dasun/OneDrive/Desktop/wheather app/weather-app/search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2")
myimage_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="c:/Users/dasun/OneDrive/Desktop/wheather app/weather-app/weather.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#bottom box
Frame_image=PhotoImage(file="c:/Users/dasun/OneDrive/Desktop/wheather app/weather-app/bottom.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

root.mainloop()

