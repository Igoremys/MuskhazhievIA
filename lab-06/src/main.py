import unittest
import random
import time
import sys

# Попытка импорта matplotlib
try:
    import matplotlib
    matplotlib.use('Agg')  # Без GUI
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("  Библиотека matplotlib не установлена. Графики не будут построены.")
    print("   Установите её: pip install matplotlib")


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Итеративная вставка. Среднее: O(log n), худшее: O(n)"""
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                # Дубликаты игнорируются
                return

    def search(self, value):
        """Итеративный поиск. Среднее: O(log n), худшее: O(n)"""
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, value):
        """Удаление (рекурсивное, но безопасное, т.к. вызывается после построения)."""
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
            min_larger = self.find_min(node.right)
            node.value = min_larger.value
            node.right = self._delete_recursive(node.right, min_larger.value)
        return node

    def find_min(self, node):
        """Поиск минимума. O(h)"""
        while node and node.left:
            node = node.left
        return node

    def find_max(self, node):
        """Поиск максимума. O(h)"""
        while node and node.right:
            node = node.right
        return node

    def height(self, node):
        """Вычисление высоты. O(n)"""
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_valid_bst(self):
        """Проверка BST. O(n)"""
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.value < high):
                return False
            return validate(node.left, low, node.value) and validate(node.right, node.value, high)
        return validate(self.root, float('-inf'), float('inf'))


# === Обходы ===
def inorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_recursive(node.left, result)
        result.append(node.value)
        inorder_recursive(node.right, result)
    return result

def preorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        preorder_recursive(node.left, result)
        preorder_recursive(node.right, result)
    return result

def postorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        postorder_recursive(node.left, result)
        postorder_recursive(node.right, result)
        result.append(node.value)
    return result

def inorder_iterative(root):
    """Итеративный in-order обход. O(n)"""
    stack, result = [], []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


# === Визуализация ===
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


# === Анализ производительности ===
def build_balanced_tree(values):
    bst = BinarySearchTree()
    shuffled = values[:]
    random.shuffle(shuffled)
    for v in shuffled:
        bst.insert(v)
    return bst

def build_degenerate_tree(values):
    bst = BinarySearchTree()
    for v in sorted(values):  # Вырожденное дерево
        bst.insert(v)
    return bst

def measure_search_time(bst, values, trials=500):
    total = 0.0
    for _ in range(trials):
        val = random.choice(values)
        start = time.perf_counter()
        bst.search(val)
        total += time.perf_counter() - start
    return total / trials

def run_performance_analysis():
    if not HAS_MATPLOTLIB:
        print("\nГрафики не будут построены (matplotlib отсутствует).")
        return

    sizes = [100, 300, 600, 1000, 1500]
    balanced_times = []
    degenerate_times = []

    print("\n Запуск эксперимента по производительности...")
    for n in sizes:
        print(f"  Тестирование дерева размером {n}...")
        values = list(range(n))
        balanced = build_balanced_tree(values)
        degenerate = build_degenerate_tree(values)

        t_bal = measure_search_time(balanced, values)
        t_deg = measure_search_time(degenerate, values)

        balanced_times.append(t_bal)
        degenerate_times.append(t_deg)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, balanced_times, label='Сбалансированное дерево', marker='o')
    plt.plot(sizes, degenerate_times, label='Вырожденное дерево', marker='x')
    plt.xlabel('Количество элементов')
    plt.ylabel('Среднее время поиска (сек)')
    plt.title('Сравнение времени поиска в BST')
    plt.legend()
    plt.grid(True)
    plt.savefig('search_time_comparison.png')
    plt.close()
    print(" График сохранён: search_time_comparison.png")


# === Тесты ===
class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        for v in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(v)

    def test_insert_and_search(self):
        self.assertIsNotNone(self.bst.search(40))
        self.assertIsNone(self.bst.search(100))

    def test_delete_leaf(self):
        self.bst.delete(20)
        self.assertIsNone(self.bst.search(20))

    def test_delete_one_child(self):
        self.bst.delete(30)
        self.assertIsNone(self.bst.search(30))
        self.assertIsNotNone(self.bst.search(40))

    def test_delete_two_children(self):
        self.bst.delete(50)
        self.assertIsNone(self.bst.search(50))
        self.assertIsNotNone(self.bst.search(60))

    def test_traversals(self):
        expected = [20, 30, 40, 50, 60, 70, 80]
        self.assertEqual(inorder_recursive(self.bst.root), expected)
        self.assertEqual(inorder_iterative(self.bst.root), expected)
        self.assertEqual(preorder_recursive(self.bst.root), [50, 30, 20, 40, 70, 60, 80])
        self.assertEqual(postorder_recursive(self.bst.root), [20, 40, 30, 60, 80, 70, 50])

    def test_is_valid_bst(self):
        self.assertTrue(self.bst.is_valid_bst())

    def test_min_max(self):
        self.assertEqual(self.bst.find_min(self.bst.root).value, 20)
        self.assertEqual(self.bst.find_max(self.bst.root).value, 80)

    def test_height(self):
        self.assertEqual(self.bst.height(self.bst.root), 2)


# === Демонстрация ===
def demo():
    print("=== Демонстрация BST ===")
    bst = BinarySearchTree()
    for v in [50, 30, 70, 20, 40]:
        bst.insert(v)

    print("Дерево:")
    print_tree(bst.root)

    print("\nIn-order (рекурсия):", inorder_recursive(bst.root))
    print("In-order (итерация):", inorder_iterative(bst.root))
    print("Pre-order:", preorder_recursive(bst.root))
    print("Post-order:", postorder_recursive(bst.root))

    print("\nМинимум:", bst.find_min(bst.root).value)
    print("Максимум:", bst.find_max(bst.root).value)
    print("Высота:", bst.height(bst.root))
    print("Корректное BST?", bst.is_valid_bst())

    print("\nУдаление узла 30:")
    bst.delete(30)
    print_tree(bst.root)


# === Запуск ===
if __name__ == "__main__":
    demo()
    print("\n" + "=" * 50)
    print("Запуск тестов...")
    unittest.main(argv=[''], exit=False, verbosity=2)

    print("\n" + "=" * 50)
    run_performance_analysis()
    print("\n Лабораторная работа завершена.")