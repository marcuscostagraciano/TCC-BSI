import time

import numpy as np

from src import merge_sort, merge_sort_fast


def main():
    arr = np.random.randint(0, 1_000_000, size=10_000_000, dtype=np.uint32)
    arr2 = np.copy(arr)
    arr3 = np.copy(arr)

    start = time.time()
    sorted(arr)
    sorted_time = time.time() - start
    print(f"Built-in sorted() time: {sorted_time:.6f} seconds")

    start = time.time()
    merge_sort(arr2)
    merge_sort_time = time.time() - start
    print(f"merge_sort() time: {merge_sort_time:.6f} seconds")

    start = time.time()
    merge_sort_fast(arr3)
    merge_sort_fast_time = time.time() - start
    print(f"merge_sort_fast() time: {merge_sort_fast_time:.6f} seconds")


if __name__ == "__main__":
    main()
