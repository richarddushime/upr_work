import sys
from load import load_strings  
names = load_strings(sys.argv[1]) 
from names import names  # list of names to search

def linear_search(values, target):
    """ Linear Search algorithm
    O(n) time complexity
    """
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1    
for name in names:
    result = linear_search(names, name)
    if result != -1:
        print(f"Found {name} at index {result}")
    else:
        print(f"{name} not found in the list")
"""
    Big O Notation Examples
    1. O(1) - Constant Time
    2. O(log n) - Logarithmic Time
    3. O(n) - Linear Time
    4. O(n log n) - Linearithmic Time
    5. O(n^2) - Quadratic Time
"""     
