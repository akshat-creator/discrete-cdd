import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to the current node
        self.h = 0  # Heuristic cost estimate from current node to end node
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    # Using Manhattan distance as heuristic
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def a_star(maze, start, end):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        # Check if we reached the end
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path from start to end

        # Explore neighbors
        neighbors = [
            (0, -1), (0, 1), (-1, 0), (1, 0)  # Up, down, left, right
        ]
        
        for offset in neighbors:
            neighbor_pos = (current_node.position[0] + offset[0], current_node.position[1] + offset[1])

            if neighbor_pos[0] < 0 or neighbor_pos[0] >= len(maze) or neighbor_pos[1] < 0 or neighbor_pos[1] >= len(maze[0]):
                continue  # Skip out-of-bounds positions

            if maze[neighbor_pos[0]][neighbor_pos[1]] != 0:
                continue  # Skip walls (non-walkable cells)

            if neighbor_pos in closed_set:
                continue  # Skip already evaluated positions

            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_pos, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # If a node with the same position is in the open list with a lower f, skip adding
            if any(open_node.position == neighbor_pos and open_node.f <= neighbor_node.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)

path = a_star(maze, start, end)
print("Path:", path)
