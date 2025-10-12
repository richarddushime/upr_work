"""
Linked List Merge Sort Implementation in Python
This module provides a function to perform merge sort on a singly linked list.
It includes the Node and LinkedList classes to create and manage the linked list structure.
"""
from inspect import getmodule
from linked_list import Node, LinkedList
def merge_sort_linked_list(linked_list):
    """
    Sorts a singly linked list in ascending order using the merge sort algorithm.
    Returns a new sorted linked list.

    Time Complexity: O(n log n)
    Space Complexity: O(log n) due to recursive stack space

    :param linked_list: LinkedList - The linked list to be sorted
    :return: LinkedList - A new sorted linked list
    """
    if linked_list.head is None or linked_list.head.next_Node is None:
        return linked_list

    # Split the linked list into two halves
    left_half, right_half = split_linked_list(linked_list)
    
    # Recursively sort both halves
    left_sorted = merge_sort_linked_list(left_half)
    right_sorted = merge_sort_linked_list(right_half)

    # Merge the sorted halves
    return merge_sorted_linked_lists(left_sorted, right_sorted)
def split_linked_list(linked_list):
    """ Splits a linked list into two halves.
    If the length is odd, the extra node goes in the first half.    
    Takes O(n) time (linear time)
    :param linked_list: LinkedList - The linked list to be split

    :return: Tuple(LinkedList, LinkedList) - Two halves of the linked list
    """
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        mid = get_middle_node(linked_list)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid.next_Node
        mid.next_Node = None
        return left_half, right_half
def get_middle_node(linked_list):
    """ Uses the fast/slow pointer strategy to find the middle node in the linked list.
    Takes O(n) time (linear time)
    :param linked_list: LinkedList - The linked list to find the middle node of

    :return: Node - The middle node of the linked list
    """
    if linked_list is None:
        return linked_list
    slow = linked_list.head
    fast = linked_list.head
    while fast.next_Node and fast.next_Node.next_Node:
        slow = slow.next_Node
        fast = fast.next_Node.next_Node
    return slow
def merge_sorted_linked_lists(left, right):
    """ Merges two sorted linked lists into one sorted linked list.
    Takes O(n) time (linear time)
    :param left: LinkedList - The first sorted linked list
    :param right: LinkedList - The second sorted linked list

    :return: LinkedList - The merged sorted linked list
    """
    merged = LinkedList()
    if left.head is None:
        return right
    if right.head is None:
        return left
    # Initialize pointers for left, right, and merged lists
    left_current = left.head
    right_current = right.head
    if left_current.data < right_current.data:
        merged.head = left_current
        left_current = left_current.next_Node
    else:
        merged.head = right_current
        right_current = right_current.next_Node
    merged_current = merged.head
    # Traverse both lists and append the smaller node to the merged list
    while left_current and right_current:
        if left_current.data < right_current.data:
            merged_current.next_Node = left_current
            left_current = left_current.next_Node
        else:
            merged_current.next_Node = right_current
            right_current = right_current.next_Node
        merged_current = merged_current.next_Node
    # Append any remaining nodes from either list
    if left_current:
        merged_current.next_Node = left_current
    if right_current:
        merged_current.next_Node = right_current
    return merged
# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.add(15)
    ll.add(10)
    ll.add(5)
    ll.add(20)
    ll.add(3)
    ll.add(2)
    print("Unsorted Linked List:")
    print(ll)
    sorted_ll = merge_sort_linked_list(ll)
    print("Sorted Linked List:")
    print(sorted_ll)    

def verify_sorted_linked_list(linked_list):
    """ 
    Helper function to verify if the linked list is sorted
    Takes O(n) time (linear time)
    """
    current = linked_list.head
    if current is None or current.next_Node is None:
        return True
    while current.next_Node:
        if current.data > current.next_Node.data:
            return False
        current = current.next_Node
    return True 

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.add(15)
    ll.add(10)
    ll.add(5)
    ll.add(20)
    ll.add(3)
    ll.add(2)
    print("Unsorted Linked List:")
    print(ll)
    sorted_ll = merge_sort_linked_list(ll)
    print("Sorted Linked List:")
    print(sorted_ll)    
    print("Is the linked list sorted?", verify_sorted_linked_list(sorted_ll))  # Output: True
    # Note: merge_sort_linked_list may mutate the original list, so this check may not always return False.
    print("Is the linked list sorted?", verify_sorted_linked_list(ll))  # May not be False if input is mutated
    