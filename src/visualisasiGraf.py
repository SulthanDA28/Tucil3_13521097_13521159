import networkx as nx
import matplotlib.pyplot as plt

# Membaca file graf
def read_graph(filename):
    with open(filename) as f:
        nodes = f.readline().strip().split()
        n = len(nodes)
        graph = nx.Graph()
        graph.add_nodes_from(nodes)
        for i in range(n):
            line = f.readline().strip().split()
            for j in range(n):
                if line[j] != '0':
                    graph.add_edge(nodes[i], nodes[j], weight=int(line[j]))
        return graph

# Membuat gambar graf
def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

# Menerima input nama file dan menggambar graf
def main():
    filename = input("Masukkan nama file graf: ")
    graph = read_graph(filename)
    draw_graph(graph)

if __name__ == "__main__":
    main()
