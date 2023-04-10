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
            if matrix[i][j] != matrix[j][i]:
                return False
            if(matrix[i][j] < 0):
                return False
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
def Astar(graph, awal, akhir, jrkheur):
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
        print("Rute : ",end="")
        for i in range(len(list)):
            if(i==len(list)-1):
                print(nama[list[i]],end="")
            else:
                print(nama[list[i]]+"->",end="")

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
            matriks[i][j] = int(matriks[i][j])
def koorstrtoint(matriks):
    for i in range(len(matriks)):
        for j in range(len(matriks[0])):
            matriks[i][j] = int(matriks[i][j])
# def jarak(graph,list):
#     hasil = 0
#     for i in range(len(list)-1):
#         hasil+=graph[list[i]][list[i+1]]
#     return hasil
namafile = input("Masukan nama file:")
n,m,k = read_file(namafile)
jrk = jarakheuristik(k,0)
matstringtoint(m)
mtog = matrixToGraph(m)
hasilastar = Astar(mtog,0,1,jrk)
print
# print(jarak(mtog,hasilastar))
printRute(hasilastar,n)



            















# graph = {
#     0 : [(1, 1), (2, 3), (3, 7)],
#     1 : [(3, 5)],
#     2 : [(3, 12)]
# }
# # heur = [1,1,1,1]
# # rute = Astar(graph,0,2,heur)
# # nama = ["A","B","C","D"]
# # print(rute)
# # printRute(rute,nama)

# namakota = ["Jakarta", "Bandung", "Surabaya", "Semarang"]

# matriks = [[0, 1, 0, 10],
#            [1, 0, 0, 0],
#             [0, 0, 0, 0],
#             [10, 0, 0, 0]]
# graph = matrixToGraph(matriks)
# heur = [3,5,2,6]
# hasil = Astar(graph,0,2,heur)
# #print(hasil)
# def seleksi(matriks,list):
#     ubah = []
    
#     for i in range(len(matriks)):
#         tiapbaris = []
#         for j in range(len(matriks[0])):
#             if i not in list or j not in list:
#                 continue
#             else:
#                 tiapbaris.append(matriks[i][j])
#         ubah.append(tiapbaris)
#     for sel in range(len(ubah)):
#         if(len(ubah[sel])==0):
#             simpan = sel
#     ubah.pop(simpan)
#     return ubah
# hasilsel = seleksi(matriks,hasil)
# printRute(hasil,namakota)
# print(hasilsel)
# # tangga,berat = graph[1][0]
# # print(tangga)
# # print(berat)
# # print(cekMatrix(matriks))
# # if(cekMatrix(matriks)):
# #     graph = matrixToGraph(matriks)
# #     printGraph(graph,namakota)
# #     print(graph)