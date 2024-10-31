import networkx as nx
import matplotlib.pyplot as plt
graph = {
    "A": {"B": 3, "F": 7, "G": 1},  # A: (0,0)
    "B": {"A": 0, "C": 4, "F": 7, "G": 1, "H": 8},  # B: (0,1)
    "C": {"B": 3, "D": 2, "G": 1, "H": 8, "I": 10},  # C: (0,2)
    "D": {"C": 4, "E": 9, "H": 8, "I": 10, "J": 3},  # D: (0,3)
    "E": {"D": 2, "I": 10, "J": 3},  # E: (0,4)

    "F": {"A": 0, "B": 3, "G": 1, "K": 4, "L": 5},  # F: (1,0)
    "G": {"A": 0, "B": 3, "C": 4, "F": 7, "H": 8, "K": 4, "L": 5, "M": 2},  # G: (1,1)
    "H": {"B": 3, "C": 4, "D": 2, "G": 1, "I": 10, "L": 5, "M": 2, "N": 6},  # H: (1,2)
    "I": {"C": 4, "D": 2, "E": 9, "H": 8, "J": 3, "M": 2, "N": 6, "O": 1},  # I: (1,3)
    "J": {"D": 2, "E": 9, "I": 10, "N": 6, "O": 1},  # J: (1,4)

    "K": {"F": 7, "G": 1, "L": 5, "P": 3, "Q": 10},  # K: (2,0)
    "L": {"F": 7, "G": 1, "H": 8, "K": 4, "M": 2, "P": 3, "Q": 10, "R": 4},  # L: (2,1)
    "M": {"G": 1, "H": 8, "I": 10, "L": 5, "N": 6, "Q": 10, "R": 4, "S": 8},  # M: (2,2)
    "N": {"H": 8, "I": 10, "J": 3, "M": 2, "O": 1, "R": 4, "S": 8, "T": 2},  # N: (2,3)
    "O": {"I": 10, "J": 3, "N": 6, "S": 8, "T": 2},  # O: (2,4)

    "P": {"K": 4, "L": 5, "Q": 10, "U": 6, "V": 2},  # P: (3,0)
    "Q": {"K": 4, "L": 5, "M": 2, "P": 3, "R": 4, "U": 6, "V": 2, "W": 1},  # Q: (3,1)
    "R": {"L": 5, "M": 2, "N": 6, "Q": 10, "S": 8, "V": 2, "W": 1, "X": 3},  # R: (3,2)
    "S": {"M": 2, "N": 6, "O": 1, "R": 4, "T": 2, "W": 1, "X": 3, "Y": 5},  # S: (3,3)
    "T": {"N": 6, "O": 1, "S": 8, "X": 3, "Y": 5},  # T: (3,4)

    "U": {"P": 3, "Q": 10, "V": 2},  # U: (4,0)
    "V": {"P": 3, "Q": 10, "R": 4, "U": 6, "W": 1},  # V: (4,1)
    "W": {"Q": 10, "R": 4, "S": 8, "V": 2, "X": 3},  # W: (4,2)
    "X": {"R": 4, "S": 8, "T": 2, "W": 1, "Y": 5},  # X: (4,3)
    "Y": {"S": 8, "T": 2, "X": 3}  # Y: (4,4)
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for node, edges in graph.items():
    for target, weight in edges.items():
        G.add_edge(node, target, weight=weight)

# Create positions for the nodes in a grid-like format for better visualization
pos = {
    "A": (0, 0), "B": (0, 1), "C": (0, 2), "D": (0, 3), "E": (0, 4),
    "F": (1, 0), "G": (1, 1), "H": (1, 2), "I": (1, 3), "J": (1, 4),
    "K": (2, 0), "L": (2, 1), "M": (2, 2), "N": (2, 3), "O": (2, 4),
    "P": (3, 0), "Q": (3, 1), "R": (3, 2), "S": (3, 3), "T": (3, 4),
    "U": (4, 0), "V": (4, 1), "W": (4, 2), "X": (4, 3), "Y": (4, 4),
}

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Graph Visualization")
plt.axis('off') 
plt.show()

graph_2 = {
    "A": {"B": 4, "C": 3},
    "B": {"A": 4, "C": 2, "D": 5},
    "C": {"A": 3, "B": 2, "D": 3, "E": 6},
    "D": {"B": 5, "C": 3, "E": 1, "F": 5},
    "E": {"C": 6, "D": 1, "G": 5},
    "F": {"D": 5, "G": 2, "Z": 7},
    "G": {"E": 5, "F": 2, "Z": 4},
    "Z": {"F": 7, "G": 4},
}

def find_distances(graph_rep, node, curr_dist): 
    distances = {}
    for target_node, dist in graph_rep[node].items():
        distances[target_node] = dist + curr_dist
    return distances


def dijkstra(graph_rep, start_node, end_node):
    distance_tracker = {node: float('inf') for node in graph_rep}
    distance_tracker[start_node] = 0
    count = 0
    paths = {start_node: []}  # Start with the start_node path initialized

    visited_nodes = []

    while len(visited_nodes) < len(graph_rep):
        count=count+1
        min_dist = float('inf')
        closest_node = None

        # Find the minimum node that hasn't been visited
        for node, dist in distance_tracker.items():
            if node not in visited_nodes and dist < min_dist:
                closest_node = node
                min_dist = dist

        if closest_node is None:  # If there's no closest node, exit the loop
            break

        visited_nodes.append(closest_node)

        distances = find_distances(graph_rep, closest_node, distance_tracker[closest_node])

        for node, dist in distances.items():
            if distance_tracker[node] > dist:
                distance_tracker[node] = dist
                # Update paths
                if closest_node == start_node:
                    paths[node] = [closest_node]  # Starting path for the new node
                else:
                    # Ensure that the closest_node path exists before appending
                    paths[node] = paths.get(closest_node, []) + [closest_node]

    # Check if the end_node was reached
    if end_node in paths:
        return (paths[end_node], distance_tracker[end_node], count)
    else:
        return ([], float('inf'))  # Return empty path and infinity distance if unreachable


print("Path from A to Y in graph 1:", dijkstra(graph, "A", "Y"))
