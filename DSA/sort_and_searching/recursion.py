def sum(numbers):
    """ Recursively sum a list of numbers 
    Takes O(n) time (linear time)
    :param numbers: List[int] - The list of numbers to be summed
    :return: int - The sum of the numbers

    call stack: recursion depth
    1. sum([1, 2, 3, 4, 5])
       - numbers: [1, 2, 3, 4, 5]
       - remaining: [2, 3, 4, 5]    
         - return 1 + sum([2, 3, 4, 5]) = 1 + 14 = 15
    2. sum([2, 3, 4, 5])
       - numbers: [2, 3, 4, 5]
       - remaining: [3, 4, 5]
         - return 2 + sum([3, 4, 5]) = 2 + 12 = 14
    3. sum([3, 4, 5])
       - numbers: [3, 4, 5]
       - remaining: [4, 5]
         - return 3 + sum([4, 5]) = 3 + 9 = 12
    4. sum([4, 5])
       - numbers: [4, 5]
       - remaining: [5]
         - return 4 + sum([5]) = 4 + 5 = 9
    5. sum([5])
       - numbers: [5]
       - remaining: []
         - return 5 + sum([]) = 5 + 0 = 5
    6. sum([])
       - numbers: [] []
       - remaining: []
         - return 0
    -----------------------------
    Base case: if numbers is empty, return 0
    Recursive case: return the first element plus the sum of the rest   
    """
    print("numbers:", numbers)
    remaining = numbers[1:]  # Make a copy of the list to avoid modifying the original
    print("remaining:", remaining)
    return numbers[0] + sum(remaining) if numbers else 0
print(sum([1, 2, 3, 4, 5]))  # Output: 15