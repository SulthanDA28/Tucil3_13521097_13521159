import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import graph

window = tk.Tk()
window.title("Find Route")


imageframe = tk.LabelFrame(window,text="Map")
imageframe.grid(column=2,row=1,rowspan=10)
Labelimage = tk.Label(imageframe,width=100,height=30)
Labelimage.pack()

labelinput = tk.Label(window,text="Input File")
labelinput.grid(column=0,row=3)
butcari = tk.Button(window,text="Select",command=lambda:cari())
butcari.grid(column=0,row=4)
cekinput = tk.Label(window,text="Dipilih dipilih")
cekinput.grid(column=0,row=5)

pilihmetod = tk.Label(window,text="Pilih Algoritma")
pilihmetod.grid(column=0,row=6)

ucs = tk.Button(window,text="UCS")
ucs.grid(column=0,row=7)
astar = tk.Button(window,text="A*")
astar.grid(column=0,row=8)

filedirect = ''
namamatrks = []
def cari():
    global filedirect
    ftypes = [('Text','*.txt')]
    filedirect = filedialog.askopenfilename(filetypes=ftypes)
    if(filedirect==''):
        cekinput.config(text='Belum ada file')
    else:
        cekinput.config(text='Mantap')
        nama,matriks,koor = graph.read_file(filedirect)
        print(nama)
        graph.matstringtoint(matriks)
        print(matriks)
        graph.koorstrtoint(koor)
        print(koor)
        global namamatrks
        namamatrks = nama

value1 = tk.StringVar(window)
value1.set("Awal")
menu1 = tk.OptionMenu(window,)
menu1.grid(column=0,row=9)

# value2 = tk.StringVar(window)
# value2.set("Akhir")
# menu2 = tk.OptionMenu(window,value=value2,variable=namamatrks)
# menu2.grid(column=0,row=10)


Result = tk.Label(window,text="Result:")
Result.grid(column=2,row=10)
HasilResult = tk.Label(window,text="")
HasilResult.grid(column=3,row=10)


judul = tk.Label(window,text="Selamat datang di pencarian rute")
judul.grid(column=0,row=0)


window.mainloop()