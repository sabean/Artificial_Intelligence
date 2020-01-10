Valid for both problem 1.1 and 1.2


The solution uses the standard search algorithm called Breadth first search (BFS). The main data structure used is queue.  


problem 1.1
Priority queue is used as the weights of the edges is given. The BFS was used to find the optimal path between the start and goal.


problem 1.2
Simple queue is used in BFS. Apart from this, three classes were created, 
	1. node: which is the each coordinate have properties like location, visited (if explored), symbol (the value "." or "X") and bound (if 	in boundary).

	2. nodeList: which is the list of nodes having properties node and type (True if the group of node touches boundary False otherwise).
	3. specialGrid: which is the matrix of the nodes.
