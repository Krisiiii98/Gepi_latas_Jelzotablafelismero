import os
import numpy as np
from PIL import Image
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
           22:'S kanyar',      
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

def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = np.argmax(model.predict(image), axis=-1)[0]
    sign = classes[pred+1]
    return sign

images = os.listdir(r'c:\Users\torok\Desktop\Gepi_latas_Jelzotablafelismero\Test_Images')
eredmeny = []
for i in images:
    path = os.path.join(r'c:\Users\torok\Desktop\Gepi_latas_Jelzotablafelismero\Test_Images', str(i))
    tipp = classify(path)
    eredmeny.append((i,tipp))

for e in eredmeny:
    print(e)


