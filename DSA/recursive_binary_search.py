"""Recursive Binary Search Implementation"""

def recursive_binary_search(list, target, low, high):
    if low > high: # high index is less than low index
        return -1  # Target not found

    mid = (low + high) // 2 # Find the middle index

    if list[mid] == target: 
        return mid  # Target found
    elif list[mid] < target:
        return recursive_binary_search(list, target, mid + 1, high)  # Search in the right half
    else:
        return recursive_binary_search(list, target, low, mid - 1)  # Search in the left half
# Time Complexity: O(log n)
# Space Complexity: O(log n)
# where n is the number of elements in the list
# Recursive binary search is a more efficient algorithm for searching in sorted datasets
# as it reduces the search space by half with each recursive call.
# It is best suited for large datasets where the list is already sorted.
# It is a more complex algorithm to implement compared to linear search,
# but it is significantly faster for large datasets.
# It is important to note that binary search requires the list to be sorted beforehand.
# RECURSSIVE DEPTH is the maximum depth of the recursion tree.(how many times the function calls itself)
# The maximum depth of recursion is log(n) where n is the number of elements in the list.
# This is because with each recursive call, the search space is halved. search has a space complexity of O(log n)
# due to the call stack used for recursion.
# Example usage:
my_list = [1, 2, 3, 4, 5]
target = 3
result = recursive_binary_search(my_list, target, 0, len(my_list) - 1)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list") 

# Note: The list must be sorted for binary search to work correctly.    
# different from linear search, which can work on unsorted lists.

# recursive vs binary search

# Both algorithms are used to find a target element in a list,
# but they differ in their approach and efficiency.
# Linear search checks each element one by one until the target is found,
# while binary search divides the search space in half with each iteration or recursion.

# Linear search has a time complexity of O(n) and is best suited for small or unsorted lists.
# Binary search has a time complexity of O(log n) and is best suited for large, sorted lists.
# Linear search is simpler to implement, while binary search is more complex but faster for large datasets.
# Linear search has a space complexity of O(1), while recursive binary

# Tail optimisation is not applicable in Python as it does not support tail call optimization.
# However, in languages that do support it, tail call optimization can help reduce the space complexity of recursive functions.
# best and worst case
# In the best-case scenario, the target element is located at the middle of the list,
# resulting in a time complexity of O(1) as it is found immediately.

# In the worst-case scenario, the target element is not present in the list,
# or it is located at one of the ends of the list, leading to a time complexity of O(log n)
# as the search space is halved with each recursive call until it is empty.
# Overall, the average-case time complexity of binary search is O(log n),
# making it significantly more efficient than linear search for large datasets.