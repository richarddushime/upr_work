import networkx as nx

# 4. (A linear-time algorithm for simplifying a multigraph; suggested.)
# A multigraph is a graph that also allows loops and mutiple edges. When describing a
# multigraph with adjacency lists, a vertex v for which uv is an edge, may appear several
# times in the adjacency list of vertex u; furthermore, v = u is also allowed.
# Let G be a multigraph given by adjacency lists and let G′ be the simple graph obtained
# from the multigraph G by removing all loops and replacing the multiple edges between
# any two vertices by a single edge. Describe a linear-time algorithm that computes the
# adjacency lists of the graph G′ from the adjacency lists of the multigraph G.
# Illustrate the algorithm on the multigraph with vertex set {1, 2, 3, 4, 5}and the following
# adjacency lists: 

# Example multigraph adjacency lists
# Vertices are 1-based: {1, 2, 3, 4, 5}
adjacency_lists = {
    1: [2, 3, 4, 2],      # multiple edges to 2, no loops
    2: [1, 3, 3],         # multiple edges to 3
    3: [1, 2, 5, 5, 3],   # multiple edges to 5, loop at 3
    4: [1, 5],            # simple edges
    5: [3, 4, 3]          # multiple edges to 3
}

def simplify_multigraph(adj_lists):
    n = len(adj_lists)
    simple_adj = {v: [] for v in adj_lists}
    for u in adj_lists:
        for v in adj_lists[u]:
            if u == v:
                continue  # skip loops
            # Add u to the beginning of v's list if not already present
            if simple_adj[v][:1] != [u]:
                simple_adj[v].insert(0, u)
    return simple_adj

simple_graph = simplify_multigraph(adjacency_lists)

# Print the simplified adjacency lists
for v in sorted(simple_graph):
    print(f"NG'({v}) = {simple_graph[v]}")

# The algorithm runs in O(|V| + |E|) time because:
# 1. We initialize the simple adjacency list in O(|V|) time.
# 2. We iterate through each vertex and its adjacency list in O(|E|) time.
# 3. Each insertion into the adjacency list is O(1) since we only check the first element.
# Thus, the overall time complexity is O(|V| + |E|).    

import matplotlib.pyplot as plt

# Create a NetworkX graph from the simplified adjacency lists
G = nx.Graph()
for u in simple_graph:
    for v in simple_graph[u]:
        if not G.has_edge(u, v):
            G.add_edge(u, v)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=14)
plt.title("Simplified Graph G'")
plt.show()