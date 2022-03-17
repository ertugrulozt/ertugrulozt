from tkinter import *

import random


window = Tk()
window.geometry('800x600')
window.title('Sans Topağı')
var= StringVar()
tb = Label(textvariable=var)
def sans():
    kazanan_numaralar = []
    artiBir = random.sample(range(1, 15), 1)

    while True:

        sayi = random.randint(1, 34)

        if sayi not in kazanan_numaralar:
            kazanan_numaralar.append(sayi)
        if len(kazanan_numaralar) == 5:
            break

    print(f'Numaralar: {sorted(kazanan_numaralar)}\nArtıBir: {artiBir}')
    var.set(f'Numaralar: {sorted(kazanan_numaralar)}\nArtıBir: {artiBir}')

button = Button(text= 'Generate',command=sans)
button.place(relx=0.3,rely=0.6,relwidth=0.4,relheight=0.1)

tb.place(relx=0.3,rely=0.3, relwidth=0.4, relheight=0.1)
window.mainloop()





