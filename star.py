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

def a_star(maze, start, end, penalty_factor=2):
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

        neighbors = [
            (0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)  # Up, down, left, right, diagonals
        ]
        
        for offset in neighbors:
            neighbor_pos = (current_node.position[0] + offset[0], current_node.position[1] + offset[1])

            # Skip out-of-bounds positions
            if neighbor_pos[0] < 0 or neighbor_pos[0] >= len(maze) or neighbor_pos[1] < 0 or neighbor_pos[1] >= len(maze[0]):
                continue

            # Use the cell's value as the cost
            cell_cost = maze[neighbor_pos[0]][neighbor_pos[1]]

            # Skip cells treated as walls (high cost)
            if cell_cost >= 10:  # Adjust threshold to avoid cells with too high a cost
                continue

            if neighbor_pos in closed_set:
                continue  # Skip already evaluated positions

            neighbor_node = Node(neighbor_pos, current_node)
            
            # Account for diagonal movement cost
            if abs(offset[0]) == 1 and abs(offset[1]) == 1:
                move_cost = cell_cost * 1.414  # Diagonal movement cost
            else:
                move_cost = cell_cost

            neighbor_node.g = current_node.g + move_cost  # Update g based on the cost of moving to this cell
            # Modify heuristic to account for cell cost with a lower penalty factor
            neighbor_node.h = heuristic(neighbor_pos, end_node.position) + (cell_cost * penalty_factor)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # If a node with the same position is in the open list with a lower f, skip adding
            if any(open_node.position == neighbor_pos and open_node.f <= neighbor_node.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None  

maze = [
    [0, 3, 4, 2, 9],
    [7, 1, 8, 10, 3],
    [4, 5, 2, 6, 10],
    [3, 10, 4, 8, 1],
    [6, 2, 1, 3, 5]
]
start = (0, 0)
end = (4, 4)

path = a_star(maze, start, end)
print("Path:", path)
