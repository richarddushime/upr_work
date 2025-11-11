import heapq
from typing import List, Tuple, Dict, Optional

def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def astar(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    A* algorithm to find shortest path in a grid from start to goal.
    
    :param grid: 2D list where 0 is free, 1 is obstacle.
    :param start: Tuple (row, col) for start position.
    :param goal: Tuple (row, col) for goal position.
    :return: List of coordinates representing the path, or None if no path exists.
    """
    rows, cols = len(grid), len(grid[0])
    
    # Possible movements: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Priority queue: (f_score, node)
    open_set = [(0, start)]  # (f_score, node)
    heapq.heapify(open_set)
    
    # Track where we came from for path reconstruction
    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
    
    # g_score[node] = cost from start to node
    g_score: Dict[Tuple[int, int], float] = {start: 0}
    
    # f_score[node] = g_score[node] + h(node)
    f_score: Dict[Tuple[int, int], float] = {start: manhattan_distance(start, goal)}
    
    # Track visited nodes
    closed_set = set()
    
    while open_set:
        current_f_score, current = heapq.heappop(open_set)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse to get start to goal
        
        closed_set.add(current)
        
        # Explore neighbors
        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            
            # Check if neighbor is within bounds and not an obstacle
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols) or grid[neighbor[0]][neighbor[1]] == 1:
                continue
                
            if neighbor in closed_set:
                continue
                
            # Cost to neighbor (uniform cost of 1)
            tentative_g_score = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Found a better path
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

# Example usage
def main():
    # Example grid: 0 = free, 1 = obstacle
    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    
    path = astar(grid, start, goal)
    if path:
        print("Path found:", path)
    else:
        print("No path exists.")

if __name__ == "__main__":
    main()

# Visualize the path on the grid
import matplotlib.pyplot as plt 
import networkx as nx

def draw_graph(graph):
    G = nx.Graph() # Create a NetworkX graph
    for u, neighbors in graph.items(): # Add edges to the graph
        for v in neighbors:  # neighbors are undirected edges
            G.add_edge(u, v)
    pos = {node: node for node in graph.keys()} # Position nodes based on their coordinates
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=8)
    plt.show()
