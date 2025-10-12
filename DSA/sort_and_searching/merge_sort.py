import sys
from load import load_numbers   
numbers = load_numbers(sys.argv[1])
print("Unsorted numbers:", numbers)

def merge_sort(values):
    """ Merge Sort algorithm
     O(n log n) time complexity
    """
    if len(values) <= 1:
        return values
    mid = len(values) // 2
    left_half = merge_sort(values[:mid])
    right_half = merge_sort(values[mid:])
    print("left_half:", left_half , "right_half:", right_half)
    sorted_array = []
    left_index, right_index = 0, 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_array.append(left_half[left_index])
            left_index += 1
        else:
            sorted_array.append(right_half[right_index])
            right_index += 1
    
    # Append any remaining elements from both halves
    sorted_array.extend(left_half[left_index:])
    sorted_array.extend(right_half[right_index:])
    
    return sorted_array

print("Sorted numbers:", merge_sort(numbers))
# How it works:
# 1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
# 2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.
#  This will be the sorted list itself.
# Merge sort is efficient and has a guaranteed time complexity of O(n log n), making it suitable for large datasets.
# It is a stable sort, meaning that it preserves the relative order of equal elements.
# However, it requires additional space for the temporary arrays used during the merging process,
# leading to a space complexity of O(n).    
