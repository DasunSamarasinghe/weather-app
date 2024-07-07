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
search_image=PhotoImage(file="search.png")
myimage=Label(image=search_image)
myimage.place(x=50,y=20)

Textfield=Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#fafafa",border=0,fg="black")
                
Textfield.place(x=50,y=40)
Textfield.focus()

search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2")
myimage_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="weather.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#bottom box
Frame_image=PhotoImage(file="bottom.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#label
Label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#91c0b2")
Label1.place(x=120,y=400)
Label1=Label(root,text="HUMADITY",font=("Helvetica",15,'bold'),fg="white",bg="#91c0b2")
Label1.place(x=250,y=400)
Label1=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#91c0b2")
Label1.place(x=430,y=400)
Label1=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#91c0b2")
Label1.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#170323")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text=".....",font=("arial",20,"bold"),bg="#edf5fa")
w.place(x=120,y=430)
h=Label(text=".....",font=("arial",20,"bold"),bg="#edf5fa")
h.place(x=250,y=430)
d=Label(text=".....",font=("arial",20,"bold"),bg="#edf5fa")
d.place(x=430,y=430)
p=Label(text=".....",font=("arial",20,"bold"),bg="#edf5fa")
p.place(x=650,y=430)
        

root.mainloop()

