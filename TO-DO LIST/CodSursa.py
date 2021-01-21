import time
import datetime
import json
import os
import sys
w=open('zile.txt', "a")
f=open('zile.txt', "r")
luniread = open("luni.txt", "r")
luni=open("luni.py", "w")
martiread = open("marti.txt", "r")
marti = open("marti.py", "w")
miercuriread = open("miercuri.txt", "r")
miercuri= open("miercuri.py", "w")
joiread = open("joi.txt", "r")
joi = open("joi.py", "w")
vineriread = open("vineri.txt", "r")
vineri= open("vineri.py", "w")
sambataread = open("sambata.txt", "r")
sambata= open("sambata.py", "w")
dumincaread = open("duminica.txt", "r")
duminica= open("duminica.py", "w")
week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
indepliniri=['da','nu','n','d']
var=0
p=0
n=0
v=0

print(datetime.datetime.now().strftime("%d-%m-%y"))

#Cerinte pe calendar

print("Daca doresti sa adaugi cerinte mai speciale intr-o anumita zi din saptamana/luna/an, alege varianta /da/:")
intrebareprima=input("")
if intrebareprima=="da":
    raspuns3=input("data dorita dd-mm-yy(d=day, m=mounth, y=year: ")
    def main():
        zp=0
        print("Lista in data "+raspuns3+" a fost deschisa!")
        data=open(raspuns3+"data.txt", "w")
        datspl=[]
        while zp == 0:
            raspuns=input("Cerinta pe ziua "+raspuns3+" : ")
            datspl.append(raspuns)
            if raspuns == "":
                zp += 1
                del (datspl[-1])
                print(datspl)
                data.write(json.dumps(datspl))
                print("Lista a fost scrisa!")
    if __name__ == '__main__':
        main()

else:
    print("OK")


#Zilele pe saptamana:Luni,Marit,Miercuri,Joi,Vineri,Smabara,Duminica
while var==0:
    if datetime.date.today().strftime("%A")=="Monday":
        var=var+1
        print("LUNI")
        luniread = open("luni.txt", "r")
        intrebari = ["da", "nu", "gata"]
        raspuns0 = input("Ai o lista?(Daca alegi varianta /nu/, lista ta va fi streasa si inlocuita de una noua): ")
        if raspuns0 == "nu":
            luni=open("luni.txt", "w")
            zii = []
            while p == 0:
                raspuns=input("Cerinta pe ziua de azi: ")
                zii.append(raspuns)
                if raspuns == "":
                    p = p + 1
                    del (zii[-1])
                    print(zii)
                    var = var + 1
            luni.write(json.dumps(zii))
            print("Lista a fost scrisa!")
        elif raspuns0=="da":
            print("OK")
            print(luniread.read())
    elif datetime.date.today().strftime("%A")=="Tuesday":
        var = var + 1
        print("MARTI")
        martiread = open("marti.txt", "r")
        intrebari = ["da", "nu", "gata"]
        raspuns0 = input("Ai o lista?(Daca alegi varianta /nu/, lista ta va fi streasa si inlocuita de una noua): ")
        if raspuns0 == "nu":
            marti = open("marti.txt", "w")
            zii = []
            while p == 0:
                raspuns = input("Cerinta pe ziua de azi: ")
                zii.append(raspuns)
                if raspuns == "":
                    p = p + 1
                    del (zii[-1])
                    print(zii)
                    var = var + 1
            marti.write(json.dumps(zii))
            print("Lista a fost scrisa!")
        elif raspuns0 == "da":
            print("OK")
            print(martiread.read())
    elif datetime.date.today().strftime("%A")=="Wednesday":
        var = var + 1
        print("MIERCURI")
        miercuriread = open("miercuri.txt", "r")
        intrebari = ["da", "nu", "gata"]
        raspuns0 = input("Ai o lista?(Daca alegi varianta /nu/, lista ta va fi streasa si inlocuita de una noua): ")
        if raspuns0 == "nu":
            miercuri= open("miercuri.txt", "w")
            zii = []
            while p == 0:
                raspuns = input("Cerinta pe ziua de azi: ")
                zii.append(raspuns)
                if raspuns == "":
                    p = p + 1
                    del (zii[-1])
                    print(zii)
                    var = var + 1
            miercuri.write(json.dumps(zii))
            print("Lista a fost scrisa!")
        elif raspuns0 == "da":
            print("OK")
            print(miercuriread.read())
    elif datetime.date.today().strftime("%A")=="Thursday":
        var = var + 1
        print("JOI")
        joiread = open("joi.txt", "r")
        intrebari = ["da", "nu", "gata"]
        raspuns0 = input("Ai o lista?(Daca alegi varianta /nu/, lista ta va fi streasa si inlocuita de una noua): ")
        if raspuns0 == "nu":
            joi= open("joi.txt", "w")
            zii = []
            while p == 0:
                raspuns = input("Cerinta pe ziua de azi: ")
                zii.append(raspuns)
                if raspuns == "":
                    p = p + 1
                    del (zii[-1])
                    print(zii)
                    var = var + 1
            joi.write(json.dumps(zii))
            print("Lista a fost scrisa!")
        elif raspuns0 == "da":
            print("OK")
            print(joiread.read())
    elif datetime.date.today().strftime("%A")=="Frpipiday":
        var = var + 1
        print("VINERI")
        vineriread = open("vineri.txt", "r")
        intrebari = ["da", "nu", "gata"]
        raspuns0 = input("Ai o lista?(Daca alegi varianta /nu/, lista ta va fi streasa si inlocuita de una noua): ")
        if raspuns0 == "nu":
            vineri= open("vineri.txt", "w")
            zii = []
            while p == 0:
                raspuns = input("Cerinta pe ziua de azi: ")
                zii.append(raspuns)
                if raspuns == "":
                    p = p + 1
                    del (zii[-1])
                    print(zii)
                    var = var + 1
            vineri.write(json.dumps(zii))
            print("Lista a fost scrisa!")
        elif raspuns0 == "da":
            print("OK")
            print(vineriread.read())
    elif datetime.date.today().strftime("%A")=="Saturday":
        var = var + 1
        print("SAMBATA")
        sambataread = open("sambata.txt", "r")
        intrebari = ["da", "nu", "gata"]
        raspuns0 = input("Ai o lista?(Daca alegi varianta /nu/, lista ta va fi streasa si inlocuita de una noua): ")
        if raspuns0 == "nu":
            sambata= open("sambata.txt", "w")
            zii = []
            while p == 0:
                raspuns = input("Cerinta pe ziua de azi: ")
                zii.append(raspuns)
                if raspuns == "":
                    p = p + 1
                    del (zii[-1])
                    print(zii)
                    var = var + 1
            sambata.write(json.dumps(zii))
            print("Lista a fost scrisa!")
        elif raspuns0 == "da":
            print("OK")
            print(sambataread.read())
    elif datetime.date.today().strftime("%A")=="Sunday":
        var = var + 1
        print("DUMINICA")
        dumincaread = open("duminica.txt", "r")
        intrebari = ["da", "nu", "gata"]
        raspuns0 = input("Ai o lista?(Daca alegi varianta /nu/, lista ta va fi streasa si inlocuita de una noua): ")
        if raspuns0 == "nu":
            duminica= open("duminica.txt", "w")
            zii = []
            while p == 0:
                raspuns = input("Cerinta pe ziua de azi: ")
                zii.append(raspuns)
                if raspuns == "":
                    p = p + 1
                    del (zii[-1])
                    print(zii)
                    var = var + 1
            duminica.write(json.dumps(zii))
            print("Lista a fost scrisa!")
        elif raspuns0 == "da":
            print("OK")
            print(dumincaread.read())

#Afisarea Datelor din calendar

def search_files(directory=os.path.dirname(sys.argv[0]), extension=''):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                print(os.path.join(name))
            elif not extension:
                print("eroare")




raspuns6=input("Dorest sa afisez datele special salvate? ")
listadata=[]
pathname = os.path.dirname(sys.argv[0])
if raspuns6=="da":
    search_files(os.path.dirname(sys.argv[0]),'data.txt' )
    raspuns5=input("ce data doresti sa fie afisata? ")
    fisierread=open(raspuns5+"data.txt", "r")
    listadata.append(fisierread.read())
    print(listadata)
else:
    print("ok")


#Faza finala
while v==0:
    raspuns2 = input("Ai indeplinit sarcinile respective? ")
    if raspuns2=="da":
        print("########")
        print("BRAVO!!!")
        print("########")
        w.write("1\n")
        text=f.read()
        text=text.split()
        len(text)
        nrzile=int(len(text))+1
        print("Respecti indeplinirile zilnice de: "+ str(nrzile) +" zile!")
        v=v+1
    elif n<2 :
        print("#########################################")
        print("TREBUIE SA-TI INDEPLINESTI SARCINILE!!!!!")
        print("#########################################")
        n=n+1
    else:
        dell=open('zile.txt', "w")
        lista=dell.write("")
        print("Datele tale vor fii strese definitiv!")
        print("###########################")
        print("DATE IN CURS DE STERGERE...")
        print("###########################")
        print("DATE STERSE!!")
        print("Respecti Indeplinirile zilnice de: "+ str(lista) +" zile!")
        v=v+1
inchidere=input("")