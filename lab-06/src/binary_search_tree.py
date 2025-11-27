class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставка узла. Среднее: O(log n), худшее: O(n)"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        """Поиск узла. Среднее: O(log n), худшее: O(n)"""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        """Удаление узла. Среднее: O(log n), худшее: O(n)"""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Узел без детей или с одним
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Узел с двумя детьми
            min_larger_node = self.find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)
        return node

    def find_min(self, node):
        """Поиск минимального значения в поддереве. O(h)"""
        while node and node.left:
            node = node.left
        return node

    def find_max(self, node):
        """Поиск максимального значения в поддереве. O(h)"""
        while node and node.right:
            node = node.right
        return node

    def height(self, node):
        """Вычисление высоты дерева. O(n)"""
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_valid_bst(self):
        """Проверка корректности BST. O(n)"""
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.value < high):
                return False
            return validate(node.left, low, node.value) and validate(node.right, node.value, high)
        return validate(self.root, float('-inf'), float('inf'))