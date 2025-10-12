import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

print("Unsorted numbers:", numbers)

def is_sorted(values):
    """ Check if the list is sorted """
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def bogo_sort(values):
    """ Bogo Sort algorithm """
    while not is_sorted(values):
        random.shuffle(values)
    return values
sorted_numbers = bogo_sort(numbers)
print("Sorted numbers:", sorted_numbers)    
