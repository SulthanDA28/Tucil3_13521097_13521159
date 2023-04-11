import heapq

def ucs(graph, start, goal):
    explored = set()
    queue = [(0, start, [])]
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in explored:
            explored.add(node)
            path = path + [node]
            if node == goal:
                return path, cost
            for neighbor in graph[node]:
                n_cost = graph[node][neighbor]
                # menggunakan prio queue sebagai dasar
                heapq.heappush(queue, (cost + n_cost, neighbor, path))
    return "No path found"

# membaca file graf
def read_graph(filename):
    with open(filename) as f:
        # membaca daftar simpul
        nodes = f.readline().strip().split()
        # membaca matriks ketetanggaan
        adjacency_matrix = []
        for line in f:
            adjacency_matrix.append(list(map(float, line.strip().split())))
        # mmebuat graf
        graph = {}
        for i in range(len(nodes)):
            node = nodes[i]
            graph[node] = {}
            for j in range(len(nodes)):
                if adjacency_matrix[i][j] != 0:
                    neighbor = nodes[j]
                    cost = adjacency_matrix[i][j]
                    graph[node][neighbor] = cost
        return graph
    
# Menerima input simpul asal dan tujuan
def get_start_goal():
    start = input("Masukkan simpul asal: ")
    goal = input("Masukkan simpul tujuan: ")
    return start, goal

# Memanggil fungsi ucs dan menampilkan hasil, fungsi utamanya
def main():
    filename = input("Masukkan nama file graf: ")
    graph = read_graph(filename)
    start, goal = get_start_goal()
    print(graph)
    path, cost = ucs(graph, start, goal)
    if path == "No path found":
        print("Tidak ditemukan jalur antara", start, "dan", goal)
    else:
        print("Jalur terpendek:", "->".join(path))
        print("Biaya jalur terpendek:", cost)

if __name__ == "__main__":
    main()
