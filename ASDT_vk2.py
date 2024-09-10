import tkinter as tk
import time
import random
import winsound
import threading
import matplotlib.pyplot as plt

maailmanennatykset = {
    1920: {'aika': 10.6, 'nimi': 'Charlie Paddock'},
    1930: {'aika': 10.3, 'nimi': 'Percy Williams'},
    1988: {'aika': 9.79, 'nimi': 'Ben Johnson'},
    2009: {'aika': 9.58, 'nimi': 'Usain Bolt'},
    2030: {'aika': 9.50, 'nimi': 'Future Runner'},     # Hypoteettinen ennätys
    2040: {'aika': 9.45, 'nimi': 'Future Runner 2'},   # Hypoteettinen ennätys
    2050: {'aika': 9.40, 'nimi': 'Future Runner 3'}    # Hypoteettinen ennätys
}

leijonat = {
    "Simba": 8.2,
    "Nala": 8.5,
    "Mufasa": 7.9,
    "Scar": 8.7,
    "Kiara": 8.4,
    "Zazu": 7.8,
    "Kovu": 8.0,
    "Sarabi": 8.6,
    "Timon": 7.5,
    "Pumbaa": 7.6
}


# Data vuosiluvuista ja maailmanennätysajoista
vuodet = list(maailmanennatykset.keys())
ajat = [maailmanennatykset[vuosi]['aika'] for vuosi in vuodet]

# Graafi maailmanennätysajoista
plt.plot(vuodet, ajat, marker='o', linestyle='-', color='b')

# Lisätään otsikot ja selitteet
plt.title("100 metrin maailmanennätysajat vuosina 1920-2050")
plt.xlabel("Vuosi")
plt.ylabel("Aika (sekunteina)")
plt.grid(True)
plt.show()


# Tkinter-ikkuna
root = tk.Tk()
root.title("Ernestin ja Kernestin Juoksu")

# Canvas juoksuradan piirtämiseksi
canvas = tk.Canvas(root, width=600, height=200, bg="white")
canvas.pack(pady=20)

# Lähtö- ja maaliviivat
canvas.create_line(50, 50, 50, 150, fill="black", width=5)  # Lähtöviiva
canvas.create_line(550, 50, 550, 150, fill="black", width=5)  # Maaliviiva

# Ernestin hahmo
ernesti_shape = canvas.create_oval(30, 90, 70, 130, fill="blue")

# Ernestin juoksufunktio
def juokse_ernesti():
    progress = 0
    ernestin_nopeus = random.uniform(9.5, 12.0)  # Satunnainen aika juoksulle
    step = 500 / ernestin_nopeus  # Askelkoko
    
    start_time = time.time()
    
    while progress < 500:
        progress += step
        canvas.move(ernesti_shape, step, 0)  # Siirretään juoksijaa
        root.update()
        winsound.Beep(100, 200)  # Matalan äänen simulaatio
        time.sleep(0.5)  # Väliaika
        
    end_time = time.time()
    total_time = end_time - start_time
    result_label.config(text=f"Ernesti juoksi 100m aikaan {total_time:.2f} sekuntia!")

# Painike Ernestin juoksulle
ernesti_button = tk.Button(root, text="Juokse Ernesti!", command=juokse_ernesti)
ernesti_button.pack(pady=10)

# Tulos
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Kernestin hahmo
kernesti_shape = canvas.create_oval(30, 140, 70, 180, fill="red")

# Kernestin juoksufunktio
def juokse_kernesti():
    progress = 0
    kernestin_nopeus = random.uniform(10.0, 13.0)  # Satunnainen aika juoksulle
    step = 500 / kernestin_nopeus  # Askelkoko
    
    start_time = time.time()
    
    while progress < 500:
        progress += step
        canvas.move(kernesti_shape, step, 0)  # Siirretään juoksijaa
        root.update()
        winsound.Beep(800, 200)  # Korkeamman äänen simulaatio
        time.sleep(0.5)  # Väliaika
        
    end_time = time.time()
    total_time = end_time - start_time
    result_label.config(text=f"Kernesti juoksi 100m aikaan {total_time:.2f} sekuntia!")

# Painike Kernestin juoksulle
kernesti_button = tk.Button(root, text="Juokse Kernesti!", command=juokse_kernesti)
kernesti_button.pack(pady=10)


def yhteis_laukaisu():
    def run_ernesti():
        juokse_ernesti()
    
    def run_kernesti():
        juokse_kernesti()
    
    # Aloita molemmat juoksut yhtä aikaa
    threading.Thread(target=run_ernesti).start()
    threading.Thread(target=run_kernesti).start()

# Painike yhteislähdölle
yhteis_laukaisu_button = tk.Button(root, text="Yhteislähtö!", command=yhteis_laukaisu)
yhteis_laukaisu_button.pack(pady=10)


root.mainloop()

