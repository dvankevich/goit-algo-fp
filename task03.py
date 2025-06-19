"""
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі,
використовуючи бінарну купу. Завдання включає створення графа, використання піраміди
для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини
до всіх інших.
"""

import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        """
        Ініціалізує граф як словник списків суміжності.
        Ключі - вершини, значення - списки кортежів (сусід, вага).
        """
        self.graph = {}

    def add_edge(self, u, v, weight):
        """
        Додає ребро до графа.
        :param u: Початкова вершина.
        :param v: Кінцева вершина.
        :param weight: Вага ребра.
        """
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        # Якщо граф неорієнтований, розкоментуйте наступний рядок
        # self.graph[v].append((u, weight))

    def dijkstra(self, start_node):
        """
        Реалізує алгоритм Дейкстри для знаходження найкоротших шляхів.
        :param start_node: Початкова вершина.
        :return: Кортеж (distances, previous_vertices)
                 distances: Словник найкоротших відстаней від start_node до всіх інших вершин.
                 previous_vertices: Словник для відновлення шляхів.
        """
        # Ініціалізація відстаней: нескінченність для всіх вершин, 0 для стартової.
        distances = {vertex: float("inf") for vertex in self.graph}
        distances[start_node] = 0

        # Словник для відстеження попередніх вершин на найкоротшому шляху
        previous_vertices = {vertex: None for vertex in self.graph}

        # Мін-купа: зберігає кортежі (відстань, вершина)
        # heapq автоматично працює як мін-купа за першим елементом кортежу
        priority_queue = [(0, start_node)]

        while priority_queue:
            # Витягуємо вершину з найменшою відстанню
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо ми вже знайшли коротший шлях до цієї вершини, пропускаємо
            if current_distance > distances[current_vertex]:
                continue

            # Розглядаємо сусідів поточної вершини
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, previous_vertices

    def reconstruct_path(self, start_node, end_node, previous_vertices):
        """
        Відновлює найкоротший шлях від start_node до end_node.
        :param start_node: Початкова вершина.
        :param end_node: Кінцева вершина.
        :param previous_vertices: Словник попередніх вершин, отриманий від dijkstra.
        :return: Список вершин, що утворюють шлях, або None, якщо шлях не існує.
        """
        path = []
        current = end_node
        while current is not None:
            path.append(current)
            if current == start_node:
                break
            current = previous_vertices[current]

        if path and path[-1] == start_node:
            return path[::-1]  # Повертаємо шлях у правильному порядку
        return None  # Шлях не знайдено


def convert_to_networkx(custom_graph_instance):
    """
    Перетворює екземпляр вашого класу Graph у об'єкт networkx.DiGraph.
    :param custom_graph_instance: Екземпляр вашого класу Graph.
    :return: Об'єкт networkx.DiGraph.
    """
    # Створюємо орієнтований граф NetworkX, оскільки ваш add_edge додає ребро в одному напрямку.
    # Якщо ви розкоментували рядок для неорієнтованого графа у add_edge, використовуйте nx.Graph()
    GNX = nx.DiGraph()

    for u, neighbors in custom_graph_instance.graph.items():
        # Додаємо вершину u, якщо її ще немає
        GNX.add_node(u)
        for v, weight in neighbors:
            GNX.add_edge(u, v, weight=weight)
            # Також переконаємося, що вершина v додана (на випадок, якщо вона є лише кінцем ребра)
            GNX.add_node(v)
    return GNX


# --- Приклад використання ---
if __name__ == "__main__":
    g = Graph()

    # Додаємо ребра до графа
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "E", 3)
    g.add_edge("C", "D", 2)
    g.add_edge("C", "F", 4)
    g.add_edge("D", "E", 3)
    g.add_edge("D", "F", 1)
    g.add_edge("E", "Z", 1)
    g.add_edge("F", "Z", 3)

    start_node = "A"
    distances, previous_vertices = g.dijkstra(start_node)

    print(f"Найкоротші відстані від вершини {start_node}:")
    for vertex, dist in distances.items():
        print(f"  До {vertex}: {dist}")

    print("\nВідновлення шляхів:")
    target_node = "Z"
    path = g.reconstruct_path(start_node, target_node, previous_vertices)
    if path:
        print(
            f"Найкоротший шлях від {start_node} до {target_node}: {' -> '.join(path)}"
        )
    else:
        print(f"Шлях від {start_node} до {target_node} не знайдено.")

    target_node_2 = "E"
    path_2 = g.reconstruct_path(start_node, target_node_2, previous_vertices)
    if path_2:
        print(
            f"Найкоротший шлях від {start_node} до {target_node_2}: {' -> '.join(path_2)}"
        )
    else:
        print(f"Шлях від {start_node} до {target_node_2} не знайдено.")

    # --- Перетворення на NetworkX граф ---
    GNX = convert_to_networkx(g)

    # --- Візуалізація графа NetworkX ---
    plt.figure(figsize=(8, 6))  # Збільшимо розмір для кращої читабельності
    pos = nx.spring_layout(GNX)  # Алгоритм розташування вузлів

    # Малюємо вузли
    nx.draw_networkx_nodes(GNX, pos, node_color="skyblue", node_size=1500)

    # Малюємо ребра
    nx.draw_networkx_edges(
        GNX, pos, edge_color="gray", arrowsize=20
    )  # arrowsize для стрілок орієнтованого графа

    # Малюємо підписи вузлів
    nx.draw_networkx_labels(GNX, pos, font_size=10, font_weight="bold")

    # Малюємо ваги ребер
    edge_labels = nx.get_edge_attributes(GNX, "weight")
    nx.draw_networkx_edge_labels(GNX, pos, edge_labels=edge_labels)

    plt.title("Візуалізація графа (NetworkX)")
    plt.axis("off")  # Вимкнути осі
    plt.show()
