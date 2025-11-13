from collections import deque

# Задача 1: Проверка сбалансированности скобок
def is_balanced_brackets(s: str) -> bool:
    """Используется стек (list). O(n) по времени и памяти."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

# Задача 2: Очередь печати
def simulate_print_queue(jobs):
    """Используется deque как очередь FIFO. O(n)."""
    queue = deque(jobs)
    processed = []
    while queue:
        job = queue.popleft()
        processed.append(f"Печать: {job}")
    return processed

# Задача 3: Проверка палиндрома с использованием дека
def is_palindrome(s: str) -> bool:
    """Используется deque для сравнения с обеих сторон. O(n)."""
    # Оставляем только буквы и цифры, в нижнем регистре
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    dq = deque(cleaned)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# Примеры использования
if __name__ == "__main__":
    print(is_balanced_brackets("([{}])"))      # True
    print(is_balanced_brackets("([)]"))        # False
    print(simulate_print_queue(["doc1", "doc2"]))  # ['Печать: doc1', 'Печать: doc2']
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("race a car"))         # False