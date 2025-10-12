# Linked Lists

# A linked list is a linear data structure where each element, called a node, contains a value and a reference (or link) 
# to the next node in the sequence. This structure allows for efficient insertion and deletion of elements,
# as nodes can be easily added or removed without the need to shift other elements, unlike arrays.  

# Linked lists can be singly linked, where each node points to the next node, or doubly linked, where each node points
# to both the next and previous nodes. They can also be circular, where the last node points back to the first node.    

# Common operations on linked lists include traversal (visiting each node in the list), insertion (adding a new node),
# deletion (removing a node), and searching (finding a node with a specific value). 
# Linked lists are widely used in various applications, such as implementing stacks and queues, managing memory,
# and representing graphs. They provide a flexible way to manage collections of data, especially when the size of the collection is dynamic and unknown in advance. 
# Example implementation of a singly linked list in Python:

class Node:
    """An object for storing a single node of a linked list.
    Models 2 attributes - data and the link to the next node in the list
    python3 -i linked_list.py  i for interactive mode and -m for running library module as a script
    this command helps load the filr and then you can run commands in the interactive shell
    """
    data = None
    next_Node  = None
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return " Node data: %s" % self.data 
    
class LinkedList:
    """ Singly linked list"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    def size(self):
        """ Returns the number of nodes in the list
        Takes O(n) time (linear time)
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_Node
        return count
    
    def add(self, data):
        """ 
        Adds a new node containing data at the head of the list 
        Takes O(1) time (constant time)
        prepend vs append
        prepend is adding at the head
        append is adding at the tail
        """
        new_node = Node(data)
        new_node.next_Node = self.head
        self.head = new_node

    def __repr__(self):
        """ Returns a string representation of the list
        Takes O(n) time (linear time)
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_Node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_Node
        return '-> '.join(nodes)
    
    def search(self, key):
        """ Search for the first node containing data that matches the key 
        Returns the node or None if not found
        Takes O(n) time (linear time)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_Node
        return None
    
    # insert  we need to traverse the list to find the position to insert
    def insert(self, data, index):
        """ Inserts a new node containing data at index position
        Insertion takes O(1) time (constant time)
        but finding the node at the insertion point takes O(n) time (linear time)

        So overall it takes O(n) time (linear time)
        If index is 0, the new node is inserted at the head of the list
        If index is greater than the size of the list, the new node is appended at the end of the list
        0 based indexing
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)
            current = self.head
            position = index
            while position > 1 and current.next_Node:
                current = current.next_Node
                position -= 1
            prev_node = current
            next_node = current.next_Node
            prev_node.next_Node = new_node
            new_node.next_Node = next_node
    

# remove
    def remove(self, key):
        """ Removes the first occurrence of a node that contains data that matches the key
        Returns the node or None if the key doesn't exist
        Takes O(n) time (linear time)
        """
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_Node
            elif current.data == key:
                found = True
                previous.next_Node = current.next_Node
            else:
                previous = current
                current = current.next_Node
        return current # returns the removed node or None if not found
    
# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list.is_empty())  # Output: True
    linked_list.add(10)
    linked_list.add(20)
    linked_list.add(30)
    print(linked_list)  # Output: [Head: 30]-> [20]-> [Tail: 10]
    print(linked_list.size())  # Output: 3
    print(linked_list.search(20))  # Output: Node data: 20
    linked_list.insert(25, 2)
    print(linked_list)  # Output: [Head: 30]-> [20]-> [25]-> [Tail: 10]
    linked_list.remove(20)
    print(linked_list)  # Output: [Head: 30]-> [25]-> [Tail: 10]
    print(linked_list.size())  # Output: 2  

