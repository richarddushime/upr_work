import sys
from load import load_numbers   
numbers = load_numbers(sys.argv[1])
print("Unsorted numbers:", numbers)

def quick_sort(values):
    """ Quick Sort algorithm
     O(n log n) time on average, O(n^2) in the worst case
    """
    if len(values) <= 1:
        return values
    print("values:", values)
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []
    pivot = values[len(values) // 2]
    for x in values:
        if x < pivot:
            less_than_pivot.append(x)
            print("less_than_pivot:", less_than_pivot)
        elif x == pivot:
            equal_to_pivot.append(x)
            print("equal_to_pivot:", equal_to_pivot)
        else:
            greater_than_pivot.append(x)
            print("greater_than_pivot:", greater_than_pivot)
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)
"""     else:
        pivot = values[len(values) // 2]
        left = [x for x in values if x < pivot]
        middle = [x for x in values if x == pivot]
        right = [x for x in values if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)     """
    
sorted_numbers = quick_sort(numbers)
print("Sorted numbers:", sorted_numbers)

# How it works:
# 1. Choose a pivot element from the array (here, we choose the middle element).
# 2. Partition the array into three lists:
#    - Elements less than the pivot
#    - Elements equal to the pivot
#    - Elements greater than the pivot
# 3. Recursively apply the same logic to the left and right lists.
# 4. Combine the sorted left list, middle list, and sorted right list to get the final sorted array.
# This implementation is not in-place and uses additional space for the left, middle, and right lists.
# For an in-place version, we would need to implement a different approach using indices.
# Quick sort is efficient for large datasets and is often faster in practice 
# than other O(n log n) algorithms like merge sort or heap sort due to 
# its cache efficiency and low constant factors.
# However, its worst-case performance is O(n^2), which can occur with poor pivot choices.
# To mitigate this, techniques like randomizing the pivot or using the median-of-three method can be employed.
# Overall, quick sort is a widely used and efficient sorting algorithm suitable for many applications.