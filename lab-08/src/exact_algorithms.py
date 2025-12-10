import itertools

# Точный 0/1 рюкзак (полный перебор, только для малых данных)
def exact_knapsack_01(items, capacity):
    n = len(items)
    best_value = 0
    best_combo = None
    for r in range(n + 1):
        for combo in itertools.combinations(range(n), r):
            total_weight = sum(items[i][1] for i in combo)
            total_value = sum(items[i][0] for i in combo)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combo = combo
    return best_value, best_combo