import networkx as nx
import matplotlib.pyplot as plt
def addTitik(graph, titik):
    if titik not in graph:
        graph[titik] = []
def addEdge(graph, titik1, titik2, berat):
    simpan = [titik2, berat]
    graph[titik1].append(simpan)

def matrixToGraph(matrix):
    graph = {}
    for i in range(len(matrix)):
        addTitik(graph, i)
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                addEdge(graph, i, j, matrix[i][j])
    return graph

def printGraph(graph, namakota):
    for titik in graph:
        for j in range(len(graph[titik])):
            print(namakota[titik], "-", namakota[graph[titik][j][0]], "berat:", graph[titik][j][1])
        

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
def cekMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # if matrix[i][j] != matrix[j][i]:
            #     return False
            # if(matrix[i][j] < 0):
            #     return False
            if i==j and matrix[i][j] != 0:
                return False
    return True

def getIDXName(list,nama):
    for i in range(len(list)):
        if(list[i]==nama):
            return i
            break
    return -1
def neighbour(node,graph):
    return graph[node]
def Astar(graph, awal, akhir, listkoor):
    jrkheur = jarakheuristik(listkoor,akhir)
    blm_semua = set([awal])
    udah_kunjungi = set([])
    parent = {}
    parent[awal] = awal
    simpan_length = {}
    simpan_length[awal] = 0

    while(len(blm_semua)>0):
        test = None
        for i in blm_semua:
            if(test==None or simpan_length[i] + jrkheur[i] < simpan_length[test] + jrkheur[test]):
                test = i
        if(test==None):
            print("Tidak menemukan rute")
            return None
        if(test==akhir):
            rute = []
            while(parent[test]!=test):
                rute.append(test)
                test = parent[test]
            rute.append(awal)
            rute.reverse()
            return rute
        for (tetangga,berat) in neighbour(test,graph):
            if(tetangga not in blm_semua and tetangga not in udah_kunjungi):
                blm_semua.add(tetangga)
                parent[tetangga] = test
                simpan_length[tetangga] = simpan_length[test] + berat
            else:
                if(simpan_length[tetangga]>simpan_length[test]+berat):
                    simpan_length[tetangga] = simpan_length[test] + berat
                    parent[tetangga] = test
                    if(tetangga in udah_kunjungi):
                        udah_kunjungi.remove(tetangga)
                        blm_semua.add(tetangga)
        blm_semua.remove(test)
        udah_kunjungi.add(test)
    print("Tidak menemukan rute")
    return None
def printRute(list,nama):
    if(list!=None):
        ngeprin = "Rute : "
        for i in range(len(list)):
            if(i==len(list)-1):
                ngeprin+=nama[list[i]]
            else:
                ngeprin += nama[list[i]]+"->"
    return ngeprin

def read_file(filename):
    with open(filename) as f:
        nama = f.readline().strip().split()
        banyak = len(nama)
        matriks = []
        koordinat = []
        for i in range(banyak):
            line = f.readline().strip().split()
            matriks.append(line)
        for j in range(banyak):
            koor = f.readline().strip().split()
            koordinat.append(koor)
        matstringtoint(matriks)
        koorstrtoint(koordinat)
        return nama,matriks,koordinat

def ecluidian(x1,x2,y1,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**(1/2)
def jarakheuristik(listkoor,tujuan):
    listjawaban = []
    for i in range(len(listkoor)):
        hasil = ecluidian(int(listkoor[i][0]),int(listkoor[tujuan][0]),int(listkoor[i][1]),int(listkoor[tujuan][1]))
        listjawaban.append(hasil)
    return listjawaban
def matstringtoint(matriks):
    for i in range(len(matriks)):
        for j in range(len(matriks[0])):
            matriks[i][j] = float(matriks[i][j])
def koorstrtoint(matriks):
    for i in range(len(matriks)):
        for j in range(len(matriks[0])):
            matriks[i][j] = float(matriks[i][j])
def jarak(graph,list):
    hasil = 0
    for i in range(len(list)-1):
        for j in range(len(graph[list[i]])):
            if(graph[list[i]][j][0]==list[i+1]):
                hasil+=graph[list[i]][j][1]
    return hasil

def visualgrafkoor(nama,matriks,koor):
    graph = nx.Graph()
    for i in range(len(nama)):
        graph.add_node(nama[i],pos=(koor[i][0],koor[i][1]))
    for j in range(len(nama)):
        for k in range(len(nama)):
            if(matriks[j][k]!=0):
                graph.add_edge(nama[j],nama[k],weight = int(matriks[j][k]) )
    return graph
def draw_graph_koor(graph):
    pos=nx.get_node_attributes(graph,'pos')
    nx.draw(graph,pos,with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
def draw_graph_koor_color(graph,hasil,nama):
    pos=nx.get_node_attributes(graph,'pos')
    nx.draw(graph,pos,with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    listedge = []
    for i in range(len(hasil)-1):
        edge = (nama[hasil[i]],nama[hasil[i+1]])
        listedge.append(edge)
    nx.draw_networkx_edges(graph,pos,edgelist = listedge,edge_color="tab:blue")




            















