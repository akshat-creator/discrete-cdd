import random
import heapq


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
    [90, 91, 1, 72, 67, 27, 22, 20, 34, 0],
]

nodes = "abcdefghij"


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


def initialization(nodes):
    # Make 100 random possible paths
    paths = []
    char_list = list(nodes)

    while len(paths) < 100:
        random.shuffle(char_list)
        new_path = "".join(char_list)

        if new_path not in paths:
            heapq.heappush(paths, (evaluation(graph, new_path, nodes), new_path))

    return paths


def selection(paths, k):

    # declare variables
    gene_pool = []

    # select ten best paths
    for _ in range(k):
        gene_pool.append(heapq.heappop(paths))

    gene_pool += random.sample(paths, k=k)

    return gene_pool


def swap(string, idx_1, idx_2):
    list_string = list(string)
    list_string[idx_1], list_string[idx_2] = list_string[idx_2], list_string[idx_1]
    string = "".join(list_string)

    return string


def pmx_crossover(parent_1, parent_2):
    # declare lists

    # print("parent 1 is", parent_1)
    # print("parent 2 is", parent_2)
    size = len(parent_1)
    # select random indices for parent 1  and parent 2
    # idx_1 = 1
    # idx_2 = 8
    idx_1 = random.choice(range(2, size - 1))
    idx_2 = random.choice(range(idx_1 + 1, size))
    child_1 = ["0" for _ in parent_1]
    child_2 = ["0" for _ in parent_1]

    # repeated indices list
    i_list = []
    j_list = []

    child_1[idx_1:idx_2] = parent_1[idx_1:idx_2]
    child_2[idx_1:idx_2] = parent_2[idx_1:idx_2]
    # print("The first index is", idx_1)
    # print("The second index is", idx_2)

    for i in range(idx_1, idx_2):
        char_1 = child_1[i]
        char_2 = child_2[i]

        if char_2 not in child_1:
            i_list.append(char_2)
            j_list.append(char_1)

    for i, char in enumerate(i_list):
        c1_char = j_list[i]
        p2_idx = parent_2.index(c1_char)
        # print("The index at p2:", child_1[p2_idx])

        if child_1[p2_idx] == "0":
            child_1[p2_idx] = char
        elif child_1[p2_idx] != "0":

            # print("e is at:", parent_2.index(child_1[p2_idx]))
            child_1[parent_2.index(child_1[p2_idx])] = char

    for i, char in enumerate(child_1):
        if char == "0":
            child_1[i] = parent_2[i]

    # print("".join(child_1))
    # print(sorted(child_1) == sorted(nodes))
    return "".join(child_1)


def crossover_function(paths, k):

    # declare offspring
    children = []

    # choose half random and half best genes in heap
    selected_genes = selection(paths, k=k)

    # randomize shuffling
    random.shuffle(x=selected_genes)

    # choose the first 2 indices and mate the genes
    while len(selected_genes) > 0:
        parent_1 = selected_genes.pop(0)
        parent_2 = selected_genes.pop(0)

        print(parent_1)
        print(parent_2)

        child_1 = pmx_crossover(parent_1[1], parent_2[1])
        child_2 = pmx_crossover(parent_2[1], parent_1[1])

        if sorted(child_1) == sorted(nodes):
            children.append(child_1)
        if sorted(child_2) == sorted(nodes):
            children.append(child_2)

    return children


def add_children(paths, children):

    while len(children) > 0:
        child = children.pop(0)
        heapq.heappush(paths, (evaluation(graph, child, nodes), child))

    return paths


def main():
    paths = initialization(nodes=nodes)

    print(paths[0][0])
    while paths[0][0] > 200:
        children = crossover_function(paths, 10)
        add_children(paths, children)

    print(paths[0])
    # parent_1 = "chebdgfjia"
    # parent_2 = "ejfdghaicb"

    # print(pmx_crossover(parent_1, parent_2))


main()


# def selection(paths):
