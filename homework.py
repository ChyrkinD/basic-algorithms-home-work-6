import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs_path(graph, start, goal):
    """Пошук у глибину (DFS) для знаходження шляху"""
    stack = [(start, [start])]  
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            stack.append((neighbor, path + [neighbor]))
    return None  

def bfs_path(graph, start, goal):
    """Пошук у ширину (BFS) для знаходження шляху"""
    queue = deque([(start, [start])])  
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))
    return None  

def dijkstra(graph, start):
    """Знаходить найкоротші відстані від стартової вершини до всіх інших."""
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]["weight"]
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
    
     
    return distances

def main():
    G_ua = nx.Graph()
    nodes_ua = ["Kharkiv","Poltava","Dnipro","Uman","Kyiv","Odessa","Lviv"]
    G_ua.add_nodes_from(nodes_ua)

    edges_ua = [("Kharkiv", "Poltava",143), ("Kharkiv", "Dnipro",221), 
                ("Poltava", "Dnipro",183), ("Poltava","Kyiv",343), ("Poltava", "Uman",420), 
                ("Dnipro", "Uman",417), ("Dnipro", "Odessa",455), 
                ("Uman", "Odessa",269), ("Uman","Kyiv",211), ("Uman","Lviv",530), 
                 ("Kyiv", "Lviv",540)
            ]           
    G_ua.add_weighted_edges_from(edges_ua)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G_ua)  
    nx.draw(G_ua, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1200, font_size=10)

    edge_labels = {(u, v): d["weight"] for u, v, d in G_ua.edges(data=True)}
    nx.draw_networkx_edge_labels(G_ua, pos, edge_labels=edge_labels, font_size=10, font_color='red')

    plt.title("Транспортна мережа України з вагами (відстані в км)")
    plt.show()

    # Аналіз основних характеристик графа
    num_nodes_ua = G_ua.number_of_nodes()
    num_edges_ua = G_ua.number_of_edges()
    degree_dict_ua = dict(G_ua.degree())
    avg_degree_ua = sum(degree_dict_ua.values()) / num_nodes_ua

    print(f"Кількість вузлів: {num_nodes_ua}")
    print(f"Кількість ребер: {num_edges_ua}")
    print(f"Середній ступінь вузла: {avg_degree_ua}")
    print(f"Ступені вузлів: {degree_dict_ua}")

    print(dfs_path(G_ua, "Dnipro", "Lviv")) 
    print(bfs_path(G_ua, "Dnipro", "Lviv")) 
    print(dijkstra(G_ua, 'Lviv'))

if __name__ == "__main__":
    main()