import random
import math
# import matplotlib.pyplot as plt


def generate_random_config(coord_nodes):
    random.shuffle(coord_nodes)
    

def get_travelled_dist(solution):
    # sourcery skip: inline-immediately-returned-variable, sum-comprehension
    distance = 0
    for i in range(len(solution) - 1):
        distance += math.dist(solution[i], solution[i + 1])

    return distance


def generate_childs_config(solution):
    childs = []
    for i in range(len(solution) - 1):
        child = solution
        # swap neighbor node
        child[i], child[i+1] = child[i+1], child[i]
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


def hill_climbing(curr_best_dist, curr_solution):
    childs = generate_childs_config(curr_solution)
    curr_best_child_dist, curr_best_child = get_best_child(childs)
    
    if curr_best_child_dist < curr_best_dist:
        return hill_climbing(curr_best_child_dist, curr_best_child)
    else:
        # print("local minimum found:", curr_solution)
        # print("local minimum dist:", curr_best_dist)
        return [curr_solution, curr_best_dist]


def main():
    coord_nodes = []

    with open("database/wi29.tsp", "r") as tsp_file:
        tsp_file_lines = tsp_file.read().splitlines()

        for line in tsp_file_lines[7:-1]:
            line_elems = line.split(" ")
            coord_nodes.append([float(line_elems[1]), float(line_elems[2])])

    best_solution = coord_nodes
    best_dist_solution = float('inf')

    for _ in range(10):
        generate_random_config(coord_nodes)
        distance = get_travelled_dist(coord_nodes)

        solution = hill_climbing(distance, coord_nodes)
        print(solution[0], solution[1])

        if (solution[1] < best_dist_solution):
            best_solution = solution[0]
            best_dist_solution = solution[1]
            print("NEW BEST", best_dist_solution)
        print("------------------------------")
    
    print("BEST ITERATION: ",best_solution, best_dist_solution)


if __name__ == "__main__":
    main()
