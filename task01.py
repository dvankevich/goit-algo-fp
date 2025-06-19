"""
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

    написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
    розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
    написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            # print(current)
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # наступний вузол
            current.next = prev
            prev = current
            current = next_node
        self.head = prev  # новий початок списку

    def insertion_sort(self):
        if self.head is None:
            return

        sorted_list = None  # Відсортований список
        current = self.head  # Поточний елемент для обробки

        while current:
            next_node = current.next  # Запам'ятати наступний елемент

            # Вставка нового вузла в відсортований список
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                search = sorted_list
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current

            current = next_node  # Перейти до наступного невідсортованого елемента

        self.head = sorted_list  # Оновити голову списку


def merge_sorted_lists(list1, list2):
    # Створюємо новий зв'язний список
    merged_head = None
    merged_tail = None

    # Вказівники на голови обох списків
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            # Додаємо вузол з першого списку
            if merged_head is None:
                merged_head = current1
                merged_tail = merged_head
            else:
                merged_tail.next = current1
                merged_tail = merged_tail.next
            current1 = current1.next
        else:
            # Додаємо вузол з другого списку
            if merged_head is None:
                merged_head = current2
                merged_tail = merged_head
            else:
                merged_tail.next = current2
                merged_tail = merged_tail.next
            current2 = current2.next

    # Додаємо залишкові вузли з першого списку, якщо є
    while current1:
        if merged_head is None:
            merged_head = current1
            merged_tail = merged_head
        else:
            merged_tail.next = current1
            merged_tail = merged_tail.next
        current1 = current1.next

    # Додаємо залишкові вузли з другого списку, якщо є
    while current2:
        if merged_head is None:
            merged_head = current2
            merged_tail = merged_head
        else:
            merged_tail.next = current2
            merged_tail = merged_tail.next
        current2 = current2.next

    # Оновлюємо голову нового списку
    merged_list = LinkedList()
    merged_list.head = merged_head
    return merged_list


def merge_sorted_lists_test():
    llist1 = LinkedList()
    llist1.insert_at_beginning(1)
    llist1.insert_at_end(3)
    llist1.insert_at_end(5)

    llist2 = LinkedList()
    llist2.insert_at_beginning(2)
    llist2.insert_at_end(4)
    llist2.insert_at_end(6)

    print("Список 1:")
    llist1.print_list()
    print("Список 2:")
    llist2.print_list()
    print("Об'єднаний список")
    merge_sorted_lists(llist1, llist2).print_list()


def reverse_list_test():
    llist = LinkedList()
    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)
    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()
    llist.reverse()
    print("Реверсивний список:")
    llist.print_list()


def insertion_sort_test():
    llist = LinkedList()
    llist.insert_at_beginning(50)
    llist.insert_at_end(20)
    llist.insert_at_end(2)
    llist.insert_at_end(25)
    llist.insert_at_end(15)
    print("Зв'язний список:")
    llist.print_list()
    print("Відсортований список:")
    llist.insertion_sort()
    llist.print_list()


if __name__ == "__main__":
    reverse_list_test()
    insertion_sort_test()
    merge_sorted_lists_test()
