'''
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

    написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
    розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
    написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
'''
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
      #print(current)
      print(current.data, end=" ")
      current = current.next
    print()

  def reverse(self):
      prev = None
      current = self.head
      while current:
          next_node = current.next # наступний вузол
          current.next = prev
          prev = current
          current = next_node
      self.head = prev  # новий початок списку


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

if __name__ == "__main__":
  reverse_list_test()