import matplotlib.pyplot as plt
import networkx as nx
from graph_representation import AdjacencyListGraph

def graph_to_nx(g: AdjacencyListGraph) -> nx.Graph:
    G = nx.DiGraph() if g.directed else nx.Graph()
    for u in g.graph:
        for v, w in g.graph[u].items():
            G.add_edge(u, v, weight=w)
    return G

def plot_graph(g: AdjacencyListGraph, title="Graph"):
    G = graph_to_nx(g)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    plt.show()

def plot_shortest_path(g: AdjacencyListGraph, start: int, end: int):
    from shortest_path import dijkstra
    dist, parents = dijkstra(g, start)
    if end not in dist:
        print("No path")
        return

    # Восстановление пути
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parents.get(cur)
    path = path[::-1]

    G = graph_to_nx(g)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color="lightblue", with_labels=True)
    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2.5)
    plt.title(f"Shortest path from {start} to {end}")
    plt.show()