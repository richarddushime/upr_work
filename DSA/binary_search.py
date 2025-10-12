def binary_search(list, target):
    """ returns the index of the target position in the list else return none """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1 # adjust the high index to mid - 1
        else:
            low = mid + 1 # adjust the low index to mid + 1
        
    return None
# Time Complexity: O(log n)
# Space Complexity: O(1)
# where n is the number of elements in the list
# Binary search is a more efficient algorithm for searching in sorted datasets
# as it reduces the search space by half with each iteration.
# It is best suited for large datasets where the list is already sorted.
# It is a more complex algorithm to implement compared to linear search,
# but it is significantly faster for large datasets.
# It is important to note that binary search requires the list to be sorted beforehand.
# Example usage:
my_list = [1, 2, 3, 4, 5]
target = 3
result = binary_search(my_list, target)
if result is not None:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
