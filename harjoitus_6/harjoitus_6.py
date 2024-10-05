import tkinter as tk
import time
import threading
import numpy as np
import matplotlib.pyplot as plt

ikkuna = tk.Tk()

ikkuna.geometry("1000x1000+200+200")

canvas = tk.Canvas(ikkuna, width=1000, height=1000,bg="blue")
saari = tk.Canvas()
canvas.pack()

saari=tk.Canvas(ikkuna, width=350, height=350, bg="goldenrod", highlightthickness=2, highlightbackground="black")
saari.place(x=325,y=90)



#MATRIISEJA

oja_e=np.zeros(shape=(100,1))
uima_allas_xx1=np.zeros(shape=(55,300))

uima_allas_xx1[50][42]=0

print(uima_allas_xx1)
print(Oja_e[0])
plt.matshow('uima_allas_xx1')
plt.show()

tiedot={}
tiedot['uima_allas'] =uima_allas_xx1
tiedot['oja_e']=oja_e
#J.N.E

kahvila_semafori=threading.Semaphore(10)
kahvila_lukko=threading.Lock()

tiedot["istumapaikat_puhtaus"]=10

def kayppa_toiletissa_asiakas():
    with kahvila_lukko:
        #dgrogheg
        time.sleep(10)

def kayppa_istumaan_asiakas():
    global tiedot
    with kahvila_semafori:
        for i in range(10):
            print("Nyt ollaan kriittisessö osiossa...")
            print("..koska paikkoja on rajoiytettu määrä!")
            tiedot['istumapaikat_puhtaus']=tiedot['istumapaikat_puhtaus']-1
            time.sleep(1);

def kayppa_istumaas_saikeistin():
    kahva=threading.Thread(target=kayppa_istumaan_asiakas)
    kahva.start()


ikkuna.mainloop()