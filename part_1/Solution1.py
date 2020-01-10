import sys
import numpy as np
import queue

def calcStartEnd(mat):
    row = len(mat)
    col = len(mat[0])
    wall = []
    for i in range(0, row):
        for j in range(0, col):
            if(mat[i][j] ==  'R'):
                st = (i,j)
            if(mat[i][j] == 'X'):
                ed = (i,j)
            if(mat[i][j] == '*'):
                wall.append((i,j))
    return st, ed, wall

def costDir(coordinate1, coordinate2):
    sideways = [(0,1), (0, -1)]
    up_down = [(1, 0), (-1, 0)]
    diagonal = [(1, 1), (-1, -1),(1, -1), (-1, 1)]
    res = (coordinate1[0] - coordinate2[0], coordinate1[1] - coordinate2[1])
    if res in up_down:
        return 6
    if res in sideways:
        return 5
    if res in diagonal:
        return 10
        
def boundaryCheck(val, row, col):
    (x, y) = val
    return 0 <= x < row and 0 <= y < col
    

def computeNeighbors(coord, wal, r, c):
    (x, y) = coord
    neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1)]
    validNeighbors = []
    for i in neighbors:
        if(boundaryCheck(i, r, c)):
            validNeighbors.append(i)
    result_neighbors = []
    for j in validNeighbors:
        if j not in wal:
            result_neighbors.append(j)
    return result_neighbors

def computeBFS(matx, st, ed, wall):
    rw = len(matx)
    cl = len(matx[0])
    temp = queue.PriorityQueue()
    temp.put(st, 0)
    visited = {}
    cumulativeCost = {}
    visited[st] = None
    cumulativeCost[st] = 0
    counter = 0
    while not temp.empty():
        current_node = temp.get()
        if(matx[current_node[0]][current_node[1]] == 'X' or (current_node == ed)):
            return visited, True
        neighbor = computeNeighbors(current_node, wall, rw, cl)

        for values in neighbor:
            new_cost = cumulativeCost[current_node] + costDir(current_node, values)
            
            if values not in cumulativeCost or new_cost < cumulativeCost[values]:
                counter +=1
                print("count: ", counter)
                cumulativeCost[values] = new_cost
                temp.put(values,new_cost)
                visited[values] = current_node
        print("...............................")
    return "No path found!", False

def construct_path(st, ed, visited):
    curr = ed
    path = []
    while(curr != st):
        path.append(curr)
        curr = visited[curr]
    path.append(st) 
    path.reverse() 
    return path

def optimalCost(pathx):
    cost = 0
    for i in range(0, len(pathx)-1):
        cost = cost + costDir(pathx[i], pathx[i+1])
    return cost


def solve_task1(input_matrix):
	# Enter your code here.
	# Return the minimum cost or return No path found!
    start, end, walls = calcStartEnd(input_matrix)
    visited_nodes, answer = computeBFS(input_matrix, start, end, walls)
    print(visited_nodes)
    if(answer):
        constructed_path = construct_path(start, end, visited_nodes)
        for i in constructed_path:
            print(i)
        return optimalCost(constructed_path)
    else:
        return visited_nodes
    return ""


# Use as many helper functions as you like


# Get input from command prompt and run the program
input_arg = sys.argv[1]
def run_program(file_name = input_arg):
    # Read the input matrix
    input_matrix = np.genfromtxt(file_name, dtype='str')
    print(input_matrix)
    
    # Your main function to solve the matrix
    print(solve_task1(input_matrix))


run_program()

# To test the result yourself,
# Open the command line tool, navigate to the folder and execute:
# python Solution1.py input_for_task1.txt
