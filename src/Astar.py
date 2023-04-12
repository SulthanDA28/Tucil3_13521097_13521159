import networkx as nx
import heapq
import matplotlib.pyplot as plt
import math
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
def Astar(graph, start, goal,listkoor,nama):
    jrkheur = jarakheuristik(listkoor,getIDXName(nama,goal))
    explored = set()
    queue = [(0, start, [])]
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in explored:
            explored.add(node)
            path = path + [node]
            if node == goal:
                return path, cost
            if(node!=goal):
                cost -= jrkheur[getIDXName(nama,node)]
            for neighbor in graph[node]:
                n_cost = graph[node][neighbor]
                # menggunakan prio queue sebagai dasar, f(n) = g(n) + h(n)
                heapq.heappush(queue, (cost + n_cost + jrkheur[getIDXName(nama,neighbor)], neighbor, path))
    return []
def jarak(graph,list):
    hasil = 0
    for i in range(len(list)-1):
        for j in range(len(graph[list[i]])):
            if(graph[list[i]][j][0]==list[i+1]):
                hasil+=graph[list[i]][j][1]
    return hasil


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

def ecluidian(x1,x2,y1,y2):#sebenarnya haversine:v
    jari = 6317000
    st = (math.sin((x2-x1)/2))**2
    dua = math.cos(x1)*math.cos(x2)*((math.sin(y2-y1)/2)**2)
    hasil = (st+dua)**(1/2)
    hasilakhir = 2*jari*math.asin(hasil)
    return hasilakhir
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

def visualgrafkoor(nama,matriks,koor):
    graph = nx.Graph()
    for i in range(len(nama)):
        graph.add_node(nama[i],pos=(koor[i][1],koor[i][0]))
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




            















