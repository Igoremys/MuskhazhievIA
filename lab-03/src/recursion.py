def factorial(n: int) -> int:
    """
    Вычисление факториала числа n рекурсивно.
    Временная сложность: O(n)
    Глубина рекурсии: n
    """
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Наивное рекурсивное вычисление n-го числа Фибоначчи.
    Временная сложность: O(2^n)
    Глубина рекурсии: n
    """
    if n < 0:
        raise ValueError("Число Фибоначчи не определено для отрицательных индексов.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(a: float, n: int) -> float:
    """
    Быстрое возведение числа a в степень n (рекурсивно).
    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, -n)
    if n % 2 == 0:
        half = power(a, n // 2)
        return half * half
    else:
        return a * power(a, n - 1)