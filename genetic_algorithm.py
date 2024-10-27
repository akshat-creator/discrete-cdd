import random

graph = [
[0, 10, 2, 9, 42, 62, 98, 36, 12, 90],
[10, 0, 51, 27, 31, 28, 64, 86, 51, 91],
[2, 51, 0, 13, 7, 95, 76, 46, 58, 1],
[9, 27, 13, 0, 9, 65, 8, 43, 70, 72],
[42, 31, 7, 9, 0, 35, 38, 83, 96, 67],
[62, 28, 95, 65, 35, 0, 84, 57, 16, 27],
[98, 64, 76, 8, 38, 84, 0, 42, 39, 22],
[36, 86, 46, 43, 83, 57, 42, 0, 75, 20],
[12, 51, 58, 70, 96, 16, 39, 75, 0, 34],
[90, 91, 1, 72, 67, 27, 22, 20, 34, 0]
]

nodes = "abcdefghij"

def initialization(nodes):
    # Make 100 random possible paths 
    paths = []
    char_list = list(nodes)

    while len(paths) < 100:
        random.shuffle(char_list)
        new_path = ''.join(char_list)
        if new_path not in paths:
            paths.append(new_path)

    return paths

def evaluation(graph, path, nodes):
    # Find the length of any path
    path_len = 0
    for index in range(len(path)):
        node_index = nodes.find(path[index])
        if index < len(path) - 1:
            next_node_index = nodes.find(path[index + 1])
        else:
            next_node_index = nodes.find(path[0])
        path_len += graph[node_index][next_node_index]
    
    return path_len