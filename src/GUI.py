import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import Astar
import UCS

window = tk.Tk()
window.title("Find Route")


imageframe = tk.LabelFrame(window,text="Map")
imageframe.grid(column=2,row=1,rowspan=10,columnspan=2)
Labelimage = tk.Label(imageframe,width=100,height=30)
Labelimage.pack()

labelinput = tk.Label(window,text="Input File")
labelinput.grid(column=0,row=2)
butcari = tk.Button(window,text="Select",command=lambda:cari())
butcari.grid(column=0,row=3)
cekinput = tk.Label(window,text="Belum ada file terpilih")
cekinput.grid(column=0,row=4)

pilihmetod = tk.Label(window,text="Pilih Algoritma")
pilihmetod.grid(column=0,row=10)

pilihtitik = tk.Label(window,text="Pilih titik")
pilihtitik.grid(column=0,row=6)

ucs = tk.Button(window,text="UCS",command=lambda:UCSalgo())
ucs.grid(column=0,row=11)
astar = tk.Button(window,text="A*",command=lambda:AstarAlgo())
astar.grid(column=0,row=12)

filedirect = ''
namamatrks = ["kosong"]
matrksglob = []
koorglob = []

def cari():
    global filedirect
    ftypes = [('Text','*.txt')]
    filedirect = filedialog.askopenfilename(filetypes=ftypes)
    head, tail = os.path.split(filedirect)
    if(filedirect==''):
        cekinput.config(text='Belum ada file')
    else:
        cekinput.config(text=tail)
        nama,matriks,koor = Astar.read_file(filedirect)
        if(Astar.cekMatrix(matriks)):
            graf = Astar.visualgrafkoor(nama,matriks,koor)
            global matrksglob
            global namamatrks
            global koorglob
            namamatrks = nama
            matrksglob = matriks
            koorglob = koor
            #-------visualisasi-----------
            f = plt.figure(figsize=(6.5, 4.45), dpi=100)
            ax = f.add_subplot(111)
            Astar.draw_graph_koor(graf)
            canvas = FigureCanvasTkAgg(f, master=window)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=2,rowspan=10)
            #----------------------------------------------
            global opsiawal,opsiakhir,click2,click
            opsiawal.destroy()
            opsiawal = tk.OptionMenu(window,click,*nama)
            opsiawal.grid(column=0,row=7)
            opsiakhir.destroy()
            opsiakhir = tk.OptionMenu(window,click2,*nama)
            opsiakhir.grid(column=0,row=8)
        else:
            HasilResult.config(text="Input masih ada yang salah")

def AstarAlgo():
    if(filedirect!=''):
        if(namamatrks[0]!="kosong" and matrksglob!=[] and koorglob!=[]):
            graph = Astar.matrixToGraph(matrksglob)
            hasil = Astar.Astar(graph,Astar.getIDXName(namamatrks,click.get()),Astar.getIDXName(namamatrks,click2.get()),koorglob)
            if(hasil!=None):
                rute = Astar.printRute(hasil,namamatrks)
                jrk = Astar.jarak(graph,hasil)
                HasilResult.config(text=rute)
                hasiljarak.config(text=jrk)
                graphvis = Astar.visualgrafkoor(namamatrks,matrksglob,koorglob)
                f = plt.figure(figsize=(6.5, 4.45), dpi=100)
                ax = f.add_subplot(111)
                Astar.draw_graph_koor_color(graphvis,hasil,namamatrks)
                canvas = FigureCanvasTkAgg(f, master=window)
                canvas.draw()
                canvas.get_tk_widget().grid(row=1, column=2,rowspan=10)
            else:
                HasilResult.config(text="Tidak menemukan rute")
                hasiljarak.config(text="")


def UCSalgo():
    if(filedirect!=''):
        graph = UCS.read_graph(filedirect)
        a = click.get()
        b = click2.get()
        if(len(UCS.ucs(graph,a,b)) > 2):
            hasil = "No path found"
        else:
            hasil, jarak = UCS.ucs(graph,a,b)
        if(hasil=="No path found"):
            HasilResult.config(text="Tidak menemukan rute")
            hasiljarak.config(text="")
        else:
            hasiljarak.config(text=jarak)
            ha = []
            rute = "Rute : "
            for j in range(len(hasil)):
                if(j==len(hasil)-1):
                    rute+=hasil[j]
                else:
                    rute+=hasil[j]+"->"
            HasilResult.config(text=rute)
            for i in range(len(hasil)):
                ha.append(Astar.getIDXName(namamatrks,hasil[i]))
            graphvis = Astar.visualgrafkoor(namamatrks,matrksglob,koorglob)
            f = plt.figure(figsize=(6.5, 4.45), dpi=100)
            ax = f.add_subplot(111)
            Astar.draw_graph_koor_color(graphvis,ha,namamatrks)
            canvas = FigureCanvasTkAgg(f, master=window)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=2,rowspan=10)
    
    



click = tk.StringVar()
click.set("Pilih Titik Awal")
opsiawal = tk.OptionMenu(window,click,*namamatrks)
opsiawal.grid(column=0,row=7)

click2 = tk.StringVar()
click2.set("Pilih Titik Akhir")
opsiakhir = tk.OptionMenu(window,click2,*namamatrks)
opsiakhir.grid(column=0,row=8)

Result = tk.Label(window,text="Result:")
Result.grid(column=0,row=13)
HasilResult = tk.Label(window,text="")
HasilResult.grid(column=1,row=13,columnspan=2)

jarak = tk.Label(window,text="Jarak:")
jarak.grid(column=0,row=15)
hasiljarak = tk.Label(window,text="")
hasiljarak.grid(column=1,row=15,columnspan=2)


judul = tk.Label(window,text="Selamat datang di pencarian rute")
judul.grid(column=0,row=0)


window.mainloop()