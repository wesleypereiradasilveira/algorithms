
import numpy as np
from time import perf_counter
from rich import print as rprint
from sorting.bubble_sort import bubble_sort

def main():
    rng = np.random.default_rng()
    values: list = list(rng.integers(low=-100, high=100, size=20, dtype=int))

    start = perf_counter()
    rprint(bubble_sort(values))
    stop = perf_counter()

    rprint(f"Elapsed time: {(stop - start):.6f}")

if __name__ == "__main__":
    main()
