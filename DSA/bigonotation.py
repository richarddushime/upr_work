"""
Big O Notation describes the upper bound of an algorithm's running time or space requirements in terms of input size (n).
It helps analyze the efficiency and scalability of algorithms.

Common Big O Notations and Examples:

1. O(1) - Constant Time
    The operation does not depend on input size.
    Example:
"""
def get_first_element(arr):
     return arr[0]

"""
2. O(log n) - Logarithmic Time
    The operation reduces the problem size each step (e.g., binary search).
    Example:
"""
def binary_search(arr, target):
     left, right = 0, len(arr) - 1
     while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
                return mid
          elif arr[mid] < target:
                left = mid + 1
          else:
                right = mid - 1
     return -1

"""
3. O(n) - Linear Time
    The operation processes each element once.
    Example:
"""
def linear_search(arr, target):
     for i, val in enumerate(arr):
          if val == target:
                return i
     return -1

"""
4. O(n log n) - Linearithmic Time
    Common in efficient sorting algorithms (e.g., merge sort).
    Example:
"""
def merge_sort(arr):
     if len(arr) <= 1:
          return arr
     mid = len(arr) // 2
     left = merge_sort(arr[:mid])
     right = merge_sort(arr[mid:])
     return merge(left, right)

def merge(left, right):
     result = []
     i = j = 0
     while i < len(left) and j < len(right):
          if left[i] < right[j]:
                result.append(left[i])
                i += 1
          else:
                result.append(right[j])
                j += 1
     result.extend(left[i:])
     result.extend(right[j:])
     return result

"""
5. O(n^2) - Quadratic Time
    Common in simple sorting algorithms (e.g., bubble sort).
    Example:
"""
def bubble_sort(arr):
     n = len(arr)
     for i in range(n):
          for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
     return arr

"""
Summary Table:
O(1)      - Constant      - Accessing array element
O(log n)  - Logarithmic   - Binary search
O(n)      - Linear        - Linear search
O(n log n)- Linearithmic  - Merge sort, quicksort (average)
O(n^2)    - Quadratic     - Bubble sort, selection sort
"""