import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    visited = set()

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def create_graph():
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("E", 3)],
        "C": [("A", 2), ("D", 2), ("F", 4)],
        "D": [("C", 2), ("E", 3), ("F", 1)],
        "E": [("B", 3), ("D", 3), ("Z", 1)],
        "F": [("C", 4), ("D", 1), ("Z", 3)],
        "Z": [("E", 1), ("F", 3)],
    }
    return graph


def visualize_graph(graph):
    G = nx.Graph()

    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, "weight")

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=2000,
        font_size=15,
        font_weight="bold",
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="red")

    plt.title("Ненаправлений граф")
    plt.show()


def main():
    graph = create_graph()
    start_vertex = "A"
    distances = dijkstra(graph, start_vertex)

    for vertex in distances:
        print(f"Відстань від {start_vertex} до {vertex} дорівнює {distances[vertex]}")

    visualize_graph(graph)


if __name__ == "__main__":
    main()
