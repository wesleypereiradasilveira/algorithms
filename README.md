# Sorting and Search Algorithms in Python

## Sorting
Sorting algorithms are a set of instructions that take an array or list as an input and arrange the items into a particular order. There are prevalent in computer science, as they are used to optimize the efficiency of other algorithms and produce human-readable output. There are many different types of sorting algorithms, each with its own advantages and disadvantages.
Some common factors that are used to compare sorting algorithms are:

- Computational complexity: the amount of time and space required by the algorithm in terms of the size of the input.
- Stability: whether the algorithm preserves the relative order of elements with equal values.
- Method: the basic technique used by the algorithm, such as comparison, exchange, insertion, merging, selection, etc.

1. Bubble Sort: compares adjacent elements and swaps them if they are in the wrong order, then repeats until the array is sorted
2. Selection Sort: finds the smallest element in the array and swaps it with the first element, then repeats for the remaining elements.
3. Insertion Sort: inserts each element into its correct position in a sorted subarray, starting from the first element.
4. Merge Sort: divides the array into two halves, recursively sorts each half, and then merges them in order.
5. Quick Sort: chooses a pivot element and partitions the array into two subarrays, one with elements smaller than the pivot and one with elements larger than the pivot, then recursively sorts each subarray.
6. Heap Sort: builds a heap (a binary tree where each node is larger than its children) from the array, then repeatedly removes the largest element from the heap and places it at the end of the array.
7. Counting Sort: counts the number of occurrences of each element in the array, then uses those counts to determine the position of each element in the sorted array.
8. Radix Sort: sorts the array by each digit or letter, starting from the least significant or rightmost one, then moving to the left.
9. Bucket Sort: distributes the elements into buckets based on some criterion, then sorts each bucket individually and concatenates them together.
