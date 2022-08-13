"""
DFS is a good approach to exhaustively search for something. It takes every path then back tracks the path.

DFS GREAT FOR if our value is hidden deep

DFS uses a stack data structure. LIFO 

Goes to a vertex (node) then it adds it's adjacency vertexes to the stack. Then pops the last element added

"""

#RUN TIME = O(V+E), Space complexity = O(V+E)  Vertex + Edges

class Graph:
    #creating a dictionary , keys will be the edges  
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)  #adding a vertex as the value, and then appending each edge as a key
    
    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack: #while stack not empty
            popVertex = stack.pop()  #don't use 0 unlke BFS because we want to remove the last element with .pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)



customDict = {  "a" : ["b","c"],
                "b" : ["a", "d", "e"],
                "c" : ["a", "e"],
                "d" : ["b", "e", "f"],
                "e" : ["d", "f", "c"],
                "f" : ["d", "e"]
               }

graph = Graph(customDict)

#visiting each vertex (node) by deepest so starts at A then next deepest so C
graph.dfs("a")
