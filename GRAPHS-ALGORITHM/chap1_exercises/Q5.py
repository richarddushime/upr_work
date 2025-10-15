import math
import networkx as nx

# 5. (The minimum dominating set problem; suggested.)
# For n ≥3, the n-cycle is the graph Cn with vertex set V (Cn) = {v1, . . . , vn}and edge set
# E(Cn) = {vivi+1 |1 ≤i ≤n−1}∪{vnv1}. Solve the problems Minimum Dominating
# Set, Minimum 2-Dominating Set, and Minimum 3-Dominating Set for the case
# when the input graph G is the cycle Cn.

import matplotlib.pyplot as plt

def draw_cycle_with_dominating_set(n, dominating_set, title):
    G = nx.cycle_graph(n)
    pos = nx.circular_layout(G)
    node_colors = ['orange' if (i+1) in dominating_set else 'lightblue' for i in range(n)]
    nx.draw(G, pos, with_labels=True, labels={i: f'v{i+1}' for i in range(n)},
            node_color=node_colors, node_size=600, font_weight='bold')
    plt.title(title)
    plt.show()

def minimum_dominating_set(n):
    # Returns the minimum dominating set for Cn
    # D1 = {v_{3i+1} | 1 ≤ 3i+1 ≤ n}
    dominating_set = [i for i in range(1, n+1) if (i-1) % 3 == 0]
    return dominating_set

def minimum_2_dominating_set(n):
    # Returns the minimum 2-dominating set for Cn
    # D2 = {v_{2i+1} | 1 ≤ 2i+1 ≤ n}
    dominating_set = [i for i in range(1, n+1) if (i-1) % 2 == 0]
    return dominating_set

def minimum_3_dominating_set(n):
    # Returns the minimum 3-dominating set for Cn (which is all vertices)
    return list(range(1, n+1))

if __name__ == "__main__":
    n = 10  # Example value, change as needed

    print("Minimum Dominating Set (size={}): {}".format(
        math.ceil(n/3), minimum_dominating_set(n)))
    print("Minimum 2-Dominating Set (size={}): {}".format(
        math.ceil(n/2), minimum_2_dominating_set(n)))
    print("Minimum 3-Dominating Set (size={}): {}".format(
        n, minimum_3_dominating_set(n)))
    
# The algorithm runs in O(n) time because:
# 1. We generate the dominating sets using list comprehensions that iterate through the range of
#    vertices from 1 to n.
# 2. Each list comprehension runs in O(n) time.
# Thus, the overall time complexity is O(n).
# The sizes of the dominating sets are:
# - Minimum Dominating Set: ⌈n/3⌉
# - Minimum 2-Dominating Set: ⌈n/2⌉
# - Minimum 3-Dominating Set: n 