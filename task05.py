import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_root, title="Binary Heap Visualization"):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]["color"] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(
        heap,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=3000,
        node_color=colors,
        font_size=10,
        font_weight="bold",
        font_color="yellow",
    )
    plt.title(title)
    plt.show()


# Створення бінарної купи
def create_heap(arr):
    nodes = [Node(key) for key in arr]
    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]  # Повертаємо корінь купи


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return "#%02x%02x%02x" % rgb_color


def get_gradient_color(start_hex, end_hex, progress):
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)

    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * progress)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * progress)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * progress)

    return rgb_to_hex((r, g, b))


# Обхід в глибину (DFS)
def dfs_traverse_and_visualize(root, start_color="#1296F0", end_color="#ADD8E6"):
    if not root:
        return

    # Створюємо копію дерева для візуалізації, щоб не змінювати оригінал
    nodes_map = {}
    q_copy = deque(
        [(root, None, None)]
    )  # (оригінальний вузол, батьківський оригінальний вузол, чи це лівий нащадок)
    while q_copy:
        orig_node, parent_node_copy, is_left = q_copy.popleft()
        new_node = Node(orig_node.val, orig_node.color)
        new_node.id = orig_node.id  # Зберігаємо оригінальний ID для відповідності
        nodes_map[orig_node.id] = new_node

        if parent_node_copy:
            if is_left:
                parent_node_copy.left = new_node
            else:
                parent_node_copy.right = new_node

        if orig_node.left:
            q_copy.append((orig_node.left, new_node, True))
        if orig_node.right:
            q_copy.append((orig_node.right, new_node, False))

    visual_root = nodes_map[root.id]

    stack = [visual_root]
    visited_order = []

    while stack:
        current_node = stack.pop()
        visited_order.append(current_node.id)

        # Додаємо правого нащадка першим, щоб лівий був зверху стеку
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    # Застосовуємо кольори на основі порядку відвідування
    num_nodes = len(visited_order)
    for i, node_id in enumerate(visited_order):
        progress = i / (num_nodes - 1) if num_nodes > 1 else 0
        nodes_map[node_id].color = get_gradient_color(start_color, end_color, progress)

    draw_heap(visual_root, "Depth-First Search (DFS) Traversal")


# Обхід в ширину (BFS)
def bfs_traverse_and_visualize(root, start_color="#1296F0", end_color="#ADD8E6"):
    if not root:
        return

    # Створюємо копію дерева для візуалізації
    nodes_map = {}
    q_copy = deque([(root, None, None)])
    while q_copy:
        orig_node, parent_node_copy, is_left = q_copy.popleft()
        new_node = Node(orig_node.val, orig_node.color)
        new_node.id = orig_node.id
        nodes_map[orig_node.id] = new_node

        if parent_node_copy:
            if is_left:
                parent_node_copy.left = new_node
            else:
                parent_node_copy.right = new_node

        if orig_node.left:
            q_copy.append((orig_node.left, new_node, True))
        if orig_node.right:
            q_copy.append((orig_node.right, new_node, False))

    visual_root = nodes_map[root.id]

    queue = deque([visual_root])
    visited_order = []

    while queue:
        current_node = queue.popleft()
        visited_order.append(current_node.id)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    # Застосовуємо кольори на основі порядку відвідування
    num_nodes = len(visited_order)
    for i, node_id in enumerate(visited_order):
        progress = i / (num_nodes - 1) if num_nodes > 1 else 0
        nodes_map[node_id].color = get_gradient_color(start_color, end_color, progress)

    draw_heap(visual_root, "Breadth-First Search (BFS) Traversal")


# Приклад використання:
heap_array = [10, 9, 8, 6, 7, 5, 4]
heap_root = create_heap(heap_array)

# print("Візуалізація обходу в глибину (DFS):")
# dfs_traverse_and_visualize(heap_root)

# print("\nВізуалізація обходу в ширину (BFS):")
# bfs_traverse_and_visualize(heap_root)

print("Візуалізація обходу в глибину (DFS):")
dfs_traverse_and_visualize(heap_root, start_color="#800080", end_color="#00FF00")

print("\nВізуалізація обходу в ширину (BFS):")
bfs_traverse_and_visualize(heap_root, start_color="#800080", end_color="#00FF00")
