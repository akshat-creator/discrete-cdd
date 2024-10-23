graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "D": 3, "E": 9},
    "C": {"A": 4},
    "D": {"B": 3, "E": 7, "F": 1},
    "E": {"B": 9, "D": 7},
    "F": {"D": 1},
}

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
    distance_tracker = {node: 1e6 for node in graph_rep}
    distance_tracker[start_node] = 0

    paths = {}

    visited_nodes = []

    while len(visited_nodes) < len(graph_rep):
        min_dist = 1e6 + 1
        closest_node = ""
        # find minimum node that hasn't been visited
        for node, dist in distance_tracker.items():
            if node not in visited_nodes:
                if dist < min_dist:
                    closest_node = node
                    min_dist = dist

        visited_nodes.append(closest_node)
        distances = find_distances(
            graph_rep, closest_node, distance_tracker[closest_node]
        )

        for node, dist in distances.items():
            if distance_tracker[node] > dist:
                distance_tracker[node] = dist
                if closest_node == start_node:
                    paths[node] = [closest_node]
                else:
                    paths[node] = paths.get(closest_node) + [closest_node]

    return (paths[end_node], distance_tracker[end_node])


print(dijkstra(graph_2, "A", "Z"))
