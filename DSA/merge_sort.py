#merge sort algorithm implementation in python
# divided into two halves, recursively sort each half, and then merge the sorted halves back together.


def merge_sort(list):
    """
    sorts a list in ascending order
    returs a new sorted list 
    Didide : find the midpoint of the list and divide into sublists
    Conquer: recursively sort the sublists created in previous step
    Combine: merge the sorted sublists created in previous step

    Time Complexity: O(n log n)
    Space Complexity: O(n) 

    Takes O(log n) time (logarithmic time) because the list is divided in half at each step
    and O(n) time (linear time) to merge the two halves 
    Overall time complexity is O(n log n)
    """
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left_half = merge_sort(list[:mid])
    right_half = merge_sort(list[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two unsorted lists into one sorted list
    Takes O(n) time (linear time)
    Returns 2 sublists left and right
    """
    left_index = 0
    right_index = 0
    merged_list = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1
    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])
    return merged_list


def verify_sorted(list):
    """ 
    Helper function to verify if the list is sorted
    Takes O(n) time (linear time)
    """
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])   


# Example usage:
if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(unsorted_list)
    print("Unsorted List:", unsorted_list)
    print("Sorted List:", sorted_list)  
    print("Is the list sorted?", verify_sorted(sorted_list))  # Output: True
    print("Is the list sorted?", verify_sorted(unsorted_list))  # Output: False
