import time
import random
import matplotlib.pyplot as plt
import numpy as np

def linear_search(arr, target):
    """
    Линейный поиск элемента в массиве.
    Возвращает индекс элемента или -1, если элемент не найден.
    """
    for i in range(len(arr)):  # O(n) - цикл по всем элементам
        if arr[i] == target:   # O(1) - сравнение
            return i           # O(1) - возврат значения
    return -1                  # O(1) - возврат значения
    # Общая сложность: O(n)

def binary_search(arr, target):
    """
    Бинарный поиск элемента в отсортированном массиве.
    Возвращает индекс элемента или -1, если элемент не найден.
    """
    left = 0                   # O(1) - инициализация
    right = len(arr) - 1       # O(1) - получение длины массива
    
    while left <= right:       # O(log n) - цикл выполняется log2(n) раз
        mid = (left + right) // 2  # O(1) - вычисление среднего индекса
        if arr[mid] == target:      # O(1) - сравнение
            return mid              # O(1) - возврат значения
        elif arr[mid] < target:     # O(1) - сравнение
            left = mid + 1          # O(1) - присваивание
        else:                       # O(1) - сравнение
            right = mid - 1         # O(1) - присваивание
    
    return -1                   # O(1) - возврат значения
    # Общая сложность: O(log n)

def generate_sorted_array(size):
    """Генерация отсортированного массива заданного размера."""
    arr = list(range(size))           # O(n) - создание массива
    return arr                        # O(1) - возврат массива

def measure_time(search_func, arr, target, repetitions=10):
    """
    Измерение среднего времени выполнения функции поиска.
    """
    total_time = 0
    
    for _ in range(repetitions):  # O(repetitions) - повторения измерений
        start_time = time.time()  # O(1) - получение времени
        search_func(arr, target)  # O(сложность поиска)
        end_time = time.time()    # O(1) - получение времени
        total_time += (end_time - start_time)  # O(1) - сложение
    
    return total_time / repetitions  # O(1) - деление

def main():
    """Основная функция для проведения экспериментов."""
    # Размеры массивов для тестирования
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
    
    # Целевые элементы для поиска (последний элемент в массиве)
    targets = [size - 1 for size in sizes]
    
    # Времена выполнения для каждого алгоритма
    linear_times = []
    binary_times = []
    
    print("Измерение времени выполнения...")
    print("Размер массива | Линейный поиск (с) | Бинарный поиск (с)")
    print("-" * 55)
    
    for i, size in enumerate(sizes):
        # Генерация отсортированного массива
        arr = generate_sorted_array(size)
        target = targets[i]
        
        # Измерение времени для линейного поиска
        linear_time = measure_time(linear_search, arr, target)
        linear_times.append(linear_time)
        
        # Измерение времени для бинарного поиска
        binary_time = measure_time(binary_search, arr, target)
        binary_times.append(binary_time)
        
        print(f"{size:12} | {linear_time:.8f} | {binary_time:.8f}")
    
    # Построение графиков
    plt.figure(figsize=(12, 5))
    
    # График 1: Линейный масштаб
    plt.subplot(1, 2, 1)
    plt.plot(sizes, linear_times, 'o-', label='Линейный поиск O(n)')
    plt.plot(sizes, binary_times, 's-', label='Бинарный поиск O(log n)')
    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение времени поиска (линейный масштаб)')
    plt.legend()
    plt.grid(True)
    
    # График 2: Логарифмический масштаб по оси Y
    plt.subplot(1, 2, 2)
    plt.plot(sizes, linear_times, 'o-', label='Линейный поиск O(n)')
    plt.plot(sizes, binary_times, 's-', label='Бинарный поиск O(log n)')
    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение времени поиска (логарифмическая ось Y)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Логарифмическая шкала по оси Y
    
    plt.tight_layout()
    plt.savefig('search_comparison.png')
    plt.show()
    
    # Анализ результатов
    print("\nАнализ результатов:")
    print("1. Линейный поиск показывает линейный рост времени с увеличением размера массива")
    print("2. Бинарный поиск показывает логарифмический рост времени")
    print("3. Для больших массивов бинарный поиск значительно эффективнее")

if __name__ == "__main__":
    main()