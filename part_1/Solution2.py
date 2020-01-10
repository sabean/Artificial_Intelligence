import sys
import numpy as np
import queue

def print_mat(mat):
    row = len(mat)
    col = len(mat[0])
    for i in range(0, row):
        for j in range(0, col):
            print(mat[i][j])
class node:
    def __init__(self):
        self.location =()
        self.symbol = ""
        self.visited = False
        self.bound = False
        self.change = False

    def add_node(self, loc, symbol):
        self.location = loc
        self.symbol = symbol
    
    def denodify(self):
        return self.location

    def possible_neighbors(self):
        (x, y) = self.location
        neighborhood = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
        return neighborhood
    
    def print_node(self):
        print("----------------")
        print("| (" + str(self.location[0]) + ", " + str(self.location[1]) + ")"+" ==> "+self.symbol+" |")
        print("----------------")

class nodeList:
    def __init__(self):
        self.nlist = []
        self.type = False # true for open which hits boundary false for closed
    
    def add_to_list(self, nodex):
        self.nlist.append(nodex)
    
    def print_nodes(self):
        for i in self.nlist:
            i.print_node()
        print("TYPE: ", self.type)
    

class specialGrid:
    def __init__(self):
        self.mat = []
        self.row = 0
        self.col = 0
        self.boundary = []
        self.cross = []
        self.dot = []

    def getNode(self, loc):
        (x, y) = loc
        return self.mat[x][y]
    
    def loc2visit(self, loc, truth):
        (x, y) = loc
        self.mat[x][y].visited = truth

    def copyNode(self, nde):
        (x, y) = nde.location
        self.mat[x][y].symbol = nde.symbol
        self.mat[x][y].visited = nde.visited
        self.mat[x][y].bound = nde.bound
        self.mat[x][y].change = nde.change


            
    def fillGrid(self, mat):
        self.row = len(mat)
        self.col = len(mat[0])
        for i in range(0, self.row):
            newMat = []
            for j in range(0, self.col):
                newNode = node()
                newNode.add_node((i, j), mat[i][j])
                if(i == 0 or j == 0 or i == self.row-1 or j == self.col-1):
                    self.boundary.append(newNode)
                    if(mat[i][j] == '.'):
                        newNode.bound = True
                if(mat[i][j] == '.'):
                    self.dot.append(newNode)
                if(mat[i][j] == 'X'):
                    newNode.visited = True
                    self.cross.append(newNode)
                newMat.append(newNode)
            self.mat.append(newMat)
    
    def boundaryCheck(self, val):
        (x, y) = val
        return 0 <= x < self.row and 0 <= y < self.col

    def neighbors(self, thisNode):
        thisNeighbors = thisNode.possible_neighbors()
        validNeighbors = filter(self.boundaryCheck, thisNeighbors)
        retNeighbor = []
        for i in validNeighbors:
            retNeighbor.append(self.getNode(i))
        return retNeighbor

    def grid_to_np(self):
        ret = []
        for i in range(0, self.row):
            val = []
            for j in range(0, self.col):
                val.append(self.mat[i][j].symbol)
            ret.append(val)
        return np.array(ret)

def computeBFS(graph, start):
    temp = queue.Queue()
    start.visited = True
    graph.copyNode(start)
    temp.put(start)
    lstnode = nodeList()

    while not temp.empty():
        current = temp.get()
        lstnode.add_to_list(current)
        print(current.bound)
        if(current.bound):
            lstnode.type = True
        for next in graph.neighbors(current):
            if(next.visited ==  False):
                temp.put(next)
                next.visited = True
    return lstnode                

def solve_task2(input_matrix):
    print(input_matrix)
    newGrid = specialGrid()
    newGrid.fillGrid(input_matrix)
    retlst = []
    for nds in newGrid.dot:
        if(nds.visited == False):
            ret = computeBFS(newGrid, nds)
            if(ret.type == False):
                retlst.append(ret)
    
    for nl in retlst:
        for nod in nl.nlist:
            (x, y) = nod.location
            newGrid.mat[x][y].symbol = "X"
            
    outmat = newGrid.grid_to_np()
    return outmat

# Use as many helper functions as you like


# Get input from command prompt and run the program
input_arg = sys.argv[1]
def run_program(filename = input_arg):
    # Read the input matrix
    input_matrix = np.genfromtxt(filename, dtype='str')
    
    # Your main function to solve the matrix
    output = solve_task2(input_matrix)

    # print the matrix to a txt file
    np.savetxt('output_for_task2.txt', output, fmt="%s")


run_program()


# To test the result yourself,
# Open the command line tool, navigate to the folder and execute:
# python Solution2.py input_for_task2.txt
