import time
import os
import random
from sorting.sorting import QuickSort
from hanoi.hanoi import Hanoi
from knapsack.knapsack import Knapsack



# MÉTRICAS
def count_lines(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

        return len(file.readlines())


def file_size(file_path):

    return round(
        os.path.getsize(file_path) / 1024,
        2
    )


# QUICKSORT
numbers = random.sample(range(1, 5001), 5000)

start = time.perf_counter()

QuickSort.sort(numbers)

end = time.perf_counter()

quicksort_time = end - start


# HANOI
start = time.perf_counter()

Hanoi.solve(
    disks=15,
    source="A",
    auxiliary="B",
    target="C"
)

end = time.perf_counter()

hanoi_time = end - start


# KNAPSACK
weights = [
    2, 5, 7, 3, 1,
    4, 6, 8, 9, 2
]

values = [
    10, 4, 8, 5, 3,
    7, 6, 9, 2, 1
]

start = time.perf_counter()

Knapsack.solve(
    capacity=20,
    weights=weights,
    values=values
)

end = time.perf_counter()

knapsack_time = end - start


# LINHAS DE CÓDIGO
sorting_lines = count_lines(
    "sorting/sorting.py"
)

hanoi_lines = count_lines(
    "hanoi/hanoi.py"
)

knapsack_lines = count_lines(
    "knapsack/knapsack.py"
)


# TAMANHO DOS MEUS ARQUIVOS
sorting_size = file_size(
    "sorting/sorting.py"
)

hanoi_size = file_size(
    "hanoi/hanoi.py"
)

knapsack_size = file_size(
    "knapsack/knapsack.py"
)


# TABELA DE MÉTRICAS
print("\n==============================================================")
print("MÉTRICAS COMPARATIVAS - PYTHON")
print("==============================================================")

print(
    f"{'Problema':<20}"
    f"{'Tempo(s)':<15}"
    f"{'Linhas':<10}"
    f"{'Tamanho(KB)':<15}"
)

print("-" * 60)

print(
    f"{'QuickSort':<20}"
    f"{quicksort_time:<15.8f}"
    f"{sorting_lines:<10}"
    f"{sorting_size:<15}"
)

print(
    f"{'Torres de Hanoi':<20}"
    f"{hanoi_time:<15.8f}"
    f"{hanoi_lines:<10}"
    f"{hanoi_size:<15}"
)

print(
    f"{'Mochila':<20}"
    f"{knapsack_time:<15.8f}"
    f"{knapsack_lines:<10}"
    f"{knapsack_size:<15}"
)

print("=" * 60)

