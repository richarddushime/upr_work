import networkx as nx

# 2. (Trees and paths; fundamental.)
# Recall that a tree is a connected acyclic graph.
# Let G be a graph. Show that G is a tree if and only if every pair of vertices in the graph
# G is connected by exactly one path.

def is_tree(graph):
    """
    Determines if the given undirected graph is a tree.
    The graph is represented as an adjacency list: {node: [neighbors]}.

    Returns True if the graph is a tree, False otherwise.
    """

    def has_cycle(v, parent, visited):
        visited.add(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                if has_cycle(neighbor, v, visited):
                    return True
            elif neighbor != parent:
                return True
        return False

    if not graph:
        return True  # An empty graph is considered a tree

    # Check for cycles and connectivity using DFS
    visited = set()
    nodes = list(graph.keys())
    if has_cycle(nodes[0], None, visited):
        return False  # Contains a cycle

    # Check if all nodes are connected
    if len(visited) != len(graph):
        return False  # Not connected

    return True

# Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.


# Example usage:
if __name__ == "__main__":
    # Tree example
    tree_graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1],
        4: [2],
        5: [2]
    }
    print(is_tree(tree_graph))  # Output: True

    # Not a tree (contains a cycle)
    cyclic_graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    print(is_tree(cyclic_graph))  # Output: False

    # Not a tree (disconnected)
    disconnected_graph = {
        1: [2],
        2: [1],
        3: []
    }
    print(is_tree(disconnected_graph))  # Output: False


import matplotlib.pyplot as plt

def draw_graph(graph, title="Graph"):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700)
    plt.title(title)
    plt.show()

# Visualize the example graphs
draw_graph(tree_graph, "Tree Graph")
draw_graph(cyclic_graph, "Cyclic Graph")
draw_graph(disconnected_graph, "Disconnected Graph")
