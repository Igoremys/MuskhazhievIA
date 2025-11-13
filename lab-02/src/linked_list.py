class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Для O(1) вставки в конец

    def insert_at_start(self, data):
        """Вставка в начало — O(1)"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """Вставка в конец — O(1) благодаря tail"""
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_start(self):
        """Удаление из начала — O(1)"""
        if not self.head:
            raise IndexError("Список пуст")
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data

    def traversal(self):
        """Обход списка — O(n)"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result