
import numpy as np
from time import perf_counter
from rich import print as rprint
from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from sorting.quick_sort import quick_sort

def main():
    rng = np.random.default_rng()
    # values: list = list(rng.integers(low=-100, high=100, size=20, dtype=int))
    values: list = [0, 5, 3, 8, -1, 6, 7, 2, 0]

    start = perf_counter()

    # rprint(f"[green bold]bubble sort[/green bold]: {bubble_sort(values)}")
    # rprint(f"[green bold]selection sort[/green bold]: {selection_sort(values)}")
    # rprint(f"[green bold]selection sort[/green bold]: {insertion_sort(values)}")
    rprint(f"[green bold]selection sort[/green bold]: {quick_sort(values)}")

    stop = perf_counter()
    rprint(f"Elapsed time: {(stop - start):.6f}")

if __name__ == "__main__":
    main()
