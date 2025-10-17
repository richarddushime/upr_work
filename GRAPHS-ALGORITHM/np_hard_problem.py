# Let us consider an example to better understand the NP class. Suppose there is a company having a total of 1000 employees having unique employee IDs. Assume that there are 200 rooms available for them. A selection of 200 employees must be paired together, but the CEO of the company has the data of some employees who can't work in the same room due to personal reasons.
# This is an example of an NP problem. Since it is easy to check if the given choice of 200 employees proposed by a coworker is satisfactory or not i.e. no pair taken from the coworker list appears on the list given by the CEO. But generating such a list from scratch seems to be so hard as to be completely impractical.

# It indicates that if someone can provide us with the solution to the problem, we can find the correct and incorrect pair in polynomial time. Thus for the NP class problem, the answer is possible, which can be calculated in polynomial time.

import networkx as nx

def verify_independent_set(forbidden_pairs, proposed_employees, k=200):
    """
    Verify if the proposed list of employees forms an independent set of size k.
    
    :param forbidden_pairs: List of tuples (i, j) where i and j cannot work together.
    :param proposed_employees: List of employee IDs (integers 0-999) proposed as the set.
    :param k: Required size (default 200).
    :return: True if valid, False otherwise.
    """
    if len(proposed_employees) != k:
        return False
    
    # Build the graph
    G = nx.Graph()
    G.add_nodes_from(range(1000))  # Employees 0 to 999
    G.add_edges_from(forbidden_pairs)
    
    # Check if any pair in proposed_employees has an edge
    for i in range(k):
        for j in range(i + 1, k):
            emp1 = proposed_employees[i]
            emp2 = proposed_employees[j]
            if G.has_edge(emp1, emp2):
                return False
    return True

# Example usage
forbidden_pairs = [(0, 1), (1, 2), (3, 4)]  # Replace with actual data
proposed = list(range(200, 400))  # Example proposed set; replace as needed
if verify_independent_set(forbidden_pairs, proposed):
    print("The proposed set is valid.")
else:
    print("The proposed set is invalid.")

    