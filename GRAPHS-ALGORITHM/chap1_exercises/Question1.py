import networkx as nx

# 1. (Basics about graphs; fundamental.)
# Prove by induction on n that every connected graph with n vertices has at least n−1
# edges.


def min_edges_connected_graph(n):
    """
    Returns the minimum number of edges in a connected graph with n vertices.
    By induction, this is always n-1.
    """
    if n < 1:
        raise ValueError("Number of vertices must be at least 1.")
    return n - 1

def is_connected(graph, n):
    """
    Checks if the undirected graph is connected.
    graph: adjacency list {vertex: [neighbors]}
    n: number of vertices
    """
    visited = set()
    def dfs(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
    # Start DFS from any vertex
    dfs(next(iter(graph)))
    return len(visited) == n

def count_edges(graph):
    """
    Counts the number of edges in an undirected graph represented as adjacency list.
    """
    return sum(len(neigh) for neigh in graph.values()) // 2

# Example usage:
if __name__ == "__main__":
    # Example: connected graph with 5 vertices (a tree)
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1],
        4: [2]
    }
    n = 5
    print("Is connected:", is_connected(graph, n))
    print("Number of edges:", count_edges(graph))
    print("Minimum required edges for connected graph:", min_edges_connected_graph(n))


import matplotlib.pyplot as plt

def draw_graph(graph):
    G = nx.Graph() # Create a NetworkX graph
    for u, neighbors in graph.items(): # Add edges to the graph
        for v in neighbors:  # neighbors are undirected edges
            G.add_edge(u, v) # u to v is an edge
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=14)
    plt.title("Graph Visualization")
    plt.show()

# Draw the example graph
draw_graph(graph)
# The algorithm runs in O(V + E) time because:
# 1. We perform a DFS which visits each vertex and edge once, taking O(V + E) time.
# 2. Counting edges involves summing the lengths of adjacency lists, which also takes O(V + E) time.
# Thus, the overall time complexity is O(V + E).
# The minimum number of edges in a connected graph with n vertices is n-1, as shown by induction:
# Base case: For n=1, a single vertex has 0 edges, which is 1-1=0.
# Inductive step: Assume true for n=k. For n=k+1, adding one vertex to a connected graph with k vertices
# requires at least one additional edge to maintain connectivity, resulting in (k-1)+1 = k edges.
# Therefore, by induction, every connected graph with n vertices has at least n-1 edges.    
# This is tight, as trees (connected acyclic graphs) have exactly n-1 edges.
