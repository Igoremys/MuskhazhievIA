import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("benchmark_results.csv")

# 1. Время от размера (для случайных данных)
plt.figure(figsize=(10, 6))
random_df = df[df["data_type"] == "random"]
sns.lineplot(data=random_df, x="size", y="time_sec", hue="algorithm", marker="o")
plt.title("Время сортировки vs Размер массива (случайные данные)")
plt.xlabel("Размер массива")
plt.ylabel("Время (сек)")
plt.yscale("log")
plt.grid(True)
plt.savefig("time_vs_size_random.png")
plt.show()

# 2. Время от типа данных (при n=5000)
n5000_df = df[df["size"] == 5000]
plt.figure(figsize=(10, 6))
sns.barplot(data=n5000_df, x="data_type", y="time_sec", hue="algorithm")
plt.title("Время сортировки по типу данных (n=5000)")
plt.ylabel("Время (сек)")
plt.yscale("log")
plt.xticks(rotation=15)
plt.grid(True, axis='y')
plt.savefig("time_vs_data_type_n5000.png")
plt.show()