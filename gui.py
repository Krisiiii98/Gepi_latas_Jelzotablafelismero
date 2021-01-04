import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy as np
from keras.models import load_model
model = load_model('modell.h5')

#Táblák elnevezése
classes = { 1:'Sebességkorlátozás (20km/h)',
            2:'Sebességkorlátozás (30km/h)',      
            3:'Sebességkorlátozás (50km/h)',       
            4:'Sebességkorlátozás (60km/h)',      
            5:'Sebességkorlátozás (70km/h)',    
            6:'Sebességkorlátozás (80km/h)',      
            7:'Sebességkorlátozás vége (80km/h)',     
            8:'Sebességkorlátozás (100km/h)',    
            9:'Sebességkorlátozás (120km/h)',     
           10:'Előzni tilos',   
           11:'Előzni tilos 3,5 tonna felett',     
           12:'Jobbkézszabály',     
           13:'Főútvonal',    
           14:'Elsőbbségadáskötelező',     
           15:'Stop',       
           16:'Autóknak behajtani tilos',       
           17:'3,5 felett behajtani tilos',       
           18:'Behajtani tilos',       
           19:'Figyelmeztető tábla',     
           20:'Éles bal kanyar',      
           21:'Éles jobb kanyar',   
           22:'Egymás utáni veszélyes útkanyarulatok',      
           23:'Dimbes Dombos út',     
           24:'Csúszós út',       
           25:'Útszűkület jobbra',  
           26:'Útmunkálatok',    
           27:'Közlekedési lámpa',      
           28:'Gyalogosok figyelem',     
           29:'Gyerekátfutás',     
           30:'Biciklisátkelő',       
           31:'Téli időben fokozott figyelem ajánlott',
           32:'Vadállatokra figyelmeztető tábla',      
           33:'Korlátozások vége',      
           34:'Kötelező haladási irány jobbra',     
           35:'Kötelező haladási irány balra',       
           36:'Kötelező haladási irány egyenesen',      
           37:'Kötelező haladási irány jobbra vagy egyenesen',      
           38:'Kötelező haladási irány balra vagy egyenesen',      
           39:'Jobbratartás',     
           40:'Balratartás',      
           41:'Körforgalom',     
           42:'Előzni tilos vége',      
           43:'3,5 tonnás súlykorlátozás vége'}
                 
#Felület létrehozása
top=tk.Tk()
top.geometry('800x600')
top.title('Közlekedési tábla felismerő')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Felismerés",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Kép betöltése",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Közlekedési tábla felismerő",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
