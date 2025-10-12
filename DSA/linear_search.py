def linear_search(list, target):
    """ returns the index of the target position in the list else return none """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of elements in the list
    

# Linear search is not a very efficient algorithm for large datasets
# as it requires checking each element one by one until the target is found.
# It is best suited for small datasets or unsorted lists where other search algorithms
# may not be applicable.
# It is a simple and easy-to-implement algorithm that can be useful in certain scenarios.
# It is also useful when the list is unsorted and we need to find an element quickly
# without sorting the list first.
# However, for larger datasets, more efficient search algorithms like binary search
# or hash tables are preferred.

# Example usage:
my_list = [4, 2, 3, 1, 5]
target = 3
result = linear_search(my_list, target)
if result is not None:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")


