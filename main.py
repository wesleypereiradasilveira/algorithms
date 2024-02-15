
import numpy as np
from time import perf_counter
from rich import print as rprint
from binary_tree.tree import Node
from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort, selection_sort_v2
from sorting.insertion_sort import insertion_sort
from sorting.quick_sort import quick_sort

def sortings():
    rng = np.random.default_rng()
    values: list = list(rng.integers(low=-100, high=100, size=20, dtype=int))
    # values: list = [0, 5, 3, 8, -1, 6, 7, 2, 0]

    rprint(f"[blue bold]original list: [/blue bold]: {values}")

    start = perf_counter()

    # rprint(f"[green bold]bubble sort[/green bold]: {bubble_sort(values)}")
    # rprint(f"[green bold]selection sort[/green bold]: {selection_sort_v2(values)}")
    # rprint(f"[green bold]selection sort[/green bold]: {insertion_sort(values)}")
    # rprint(f"[green bold]selection sort[/green bold]: {quick_sort(values)}")

    stop = perf_counter()
    rprint(f"Elapsed time: {(stop - start):.6f}")

def binary_trees():
    root = Node("g")
    root.insert("c")
    root.insert("b")
    root.insert("a")
    root.insert("e")
    root.insert("d")
    root.insert("f")
    root.insert("i")
    root.insert("h")
    root.insert("j")
    root.insert("k")
    print(root.left.__dict__)
    print(root.right.__dict__)

if __name__ == "__main__":
    # sortings()
    binary_trees()
