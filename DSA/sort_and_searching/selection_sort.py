"""
unsorted to sorted
selection sort
O(n^2) time (quadratic time)
"""

import sys
from load import load_numbers   
numbers = load_numbers(sys.argv[1])

print("Unsorted numbers:", numbers)

def selection_sort(values):
    """ Selection Sort algorithm """
    n = len(values)
    for i in range(n):
        min_index = i
        print("min_index:", min_index)
        for j in range(i + 1, n):
            if values[j] < values[min_index]:
                min_index = j
                print("new min_index:", min_index)
        # Swap the found minimum element with the first element
        values[i], values[min_index] = values[min_index], values[i]
        print(f"Step {i + 1}: {values}")
    return values

sorted_numbers = selection_sort(numbers)
print("Sorted numbers:", sorted_numbers)