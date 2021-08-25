import random
import math
import copy
# import matplotlib.pyplot as plt


def main():
    coord_nodes = []

    # obtendo nós das coordenadas do dataset
    with open("database/wi29.tsp", "r") as tsp_file:
        tsp_file_lines = tsp_file.read().splitlines()

        for line in tsp_file_lines[7:-1]:
            line_elems = line.split(" ")
            coord_nodes.append([float(line_elems[1]), float(line_elems[2])])

    best_solution = coord_nodes
    best_dist_solution = float('inf')

    for _ in range(10):
        random_config = generate_random_config(coord_nodes)
        distance = get_travelled_dist(random_config)

        solution, dist_solution, iter_num = hill_climbing(distance, random_config, 1)

        # print(solution)
        print("distance: ", dist_solution, ", number of iter: ", iter_num)

        if (dist_solution < best_dist_solution):
            best_solution = solution
            best_dist_solution = dist_solution
            print("NEW BEST", best_dist_solution)
        print("------------------------------")
    
    print("BEST ITERATION: ",best_solution, best_dist_solution)


def generate_random_config(coord_nodes):
    random_config = copy.deepcopy(coord_nodes)
    random.shuffle(random_config)
    return random_config
    

def get_travelled_dist(solution):
    distance = 0
    for i in range(len(solution) - 1):
        distance += math.dist(solution[i], solution[i + 1])

    return distance


def generate_childs_config(solution):
    n_swap_pairs = 3
    childs = []

    for _ in range(1000):
        child = copy.deepcopy(solution)

        swaps = random.sample(range(len(child)), n_swap_pairs*2)
        random.shuffle(swaps)
        
        for i in range(n_swap_pairs):
            child[swaps[i]], child[swaps[i+n_swap_pairs]] = child[swaps[i+n_swap_pairs]], child[swaps[i]]

        childs.append(child)

    return childs


def get_best_child(childs):
    curr_best_child_dist = float('inf')
    curr_best_child = []

    for child in childs:
        child_dist = get_travelled_dist(child)
        if child_dist < curr_best_child_dist:
            curr_best_child_dist = child_dist
            curr_best_child = child
    
    return curr_best_child_dist, curr_best_child


def hill_climbing(curr_best_dist, curr_solution, iter_num):
    childs = generate_childs_config(curr_solution)
    curr_best_child_dist, curr_best_child = get_best_child(childs)
    if curr_best_child_dist < curr_best_dist:
        return hill_climbing(curr_best_child_dist, curr_best_child, iter_num+1)
    else:
        # print("local minimum found:", curr_solution)
        # print("local minimum dist:", curr_best_dist)
        return [curr_solution, curr_best_dist, iter_num]
    

if __name__ == "__main__":
    main()
