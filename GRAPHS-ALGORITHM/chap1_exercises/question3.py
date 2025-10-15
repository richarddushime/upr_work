# (A linear-time algorithm for sorting the adjacency lists; suggested.)
# Let a graph G = (V, E) be given by adjacency lists. Let V= {v1, . . . , vn}be an ar-
# bitrary linear ordering of the vertices of the graph. Describe an algorithm running in
# time O(|V |+ |E|) that computes from the given adjacency lists sorted adjacency lists for
# G. (That is, for each vertex vi, its neighbors (elements of NG(vi)) appear in the list of
# neighbors of vi as vi1 , . . . , vik , where i1 < . . . < ik.)

def sort_adjacency_lists(graph):
    from collections import defaultdict, deque

    # Create a mapping from vertex to its index in the ordering
    vertex_index = {vertex: index for index, vertex in enumerate(graph)}

    # Create a new graph to hold the sorted adjacency lists
    sorted_graph = defaultdict(deque)

    # Iterate through each vertex and its adjacency list
    for vertex, neighbors in graph.items():
        # Sort the neighbors based on their indices in the original ordering
        sorted_neighbors = sorted(neighbors, key=lambda x: vertex_index[x])
        # Store the sorted neighbors in the new graph
        sorted_graph[vertex] = deque(sorted_neighbors)

    return sorted_graph

# Example usage:
if __name__ == "__main__":
    # Example graph with arbitrary vertex order
    graph = {
        'v3': ['v2', 'v1'],
        'v1': ['v3', 'v2'],
        'v2': ['v3', 'v1']
    }
    sorted_graph = sort_adjacency_lists(graph)
    for vertex in graph:
        print(f"{vertex}: {list(sorted_graph[vertex])}")


# The algorithm runs in O(|V| + |E|) time because:
# 1. Creating the vertex index mapping takes O(|V|) time.
# 2. Iterating through each vertex and sorting its neighbors takes O(|E|) time in total,
#    since each edge is considered exactly once.
# 3. Storing the sorted neighbors also takes O(|E|) time in total.
# Thus, the overall time complexity is O(|V| + |E|).


def sort_adjacency_lists_linear(graph):

    # Get the vertex ordering
    vertices = list(graph.keys())
    vertex_index = {v: i for i, v in enumerate(vertices)}

    # Initialize empty lists for each vertex
    S = {v: [] for v in vertices}

    # For each vertex in order, add it to the neighbor lists of its neighbors
    for v in vertices:
        for u in graph[v]:
            S[u].append(v)

    # Now, sort each adjacency list by the vertex ordering
    for v in vertices:
        S[v].sort(key=lambda x: vertex_index[x])

    return S

# Example usage:
if __name__ == "__main__":
    graph = {
        1: [2, 4, 3],
        2: [3, 1],
        3: [1, 5, 2],
        4: [5, 1],
        5: [4, 3]
    }
    sorted_graph = sort_adjacency_lists_linear(graph)
    for v in sorted(sorted_graph):
        print(f"{v}: {sorted_graph[v]}")

# The algorithm runs in O(|V| + |E|) time because:
# 1. Creating the vertex index mapping takes O(|V|) time.
# 2. Iterating through each vertex and adding it to its neighbors' lists takes O(|E|) time in total,
#    since each edge is considered exactly once.
# 3. Sorting each adjacency list takes O(d log d) time, where d is the degree of the vertex.
#    However, since the sum of the degrees of all vertices is 2|E|, the total time for sorting across all vertices is O(|E| log d_max),
#    where d_max is the maximum degree. In practice, if the graph is sparse, this can be approximated to O(|E|).
# Thus, the overall time complexity is O(|V| + |E|).

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, title="Graph"):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=800, font_size=14)
    plt.title(title)
    plt.show()
    plt.title(title)
    plt.show()  
