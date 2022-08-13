"""
BFS starts at traversing of an arbitray node and then goes by levels 

  Level 1      A ________C
                |         |
                |         |
                |         |
  Level 2       B ------- D


BFS starts at like A->C Next to Level 2 A->C->B->D

Implemented using a queue data structure, FIFO 

It traverses while queue is not empty, so adds the vertex to the queue, then after visiting all it's edges it removes it from queue.

Use cases: BFS conversely is useful when you're looking for a specific thing like edges. Much faster than DFS. Great if we need to find somethings close to 
starting point

Great for directed and undirected graph
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

    def bfs(self, vertex):
        visited = [vertex]  #
        queue = [vertex]   #queue
        while queue:  #while it's not null, important to keep going till all vertex have been visited   Run time = O(V)
            deVertex =  queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:  #looping through  run time = O(E)
                if adjacentVertex not in visited: 
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)


customDict = {  "a" : ["b","c"],
                "b" : ["a", "d", "e"],
                "c" : ["a", "e"],
                "d" : ["b", "e", "f"],
                "e" : ["d", "f", "c"],
                "f" : ["d", "e"]
               }

graph = Graph(customDict)

#visiting each part of the graph from level by level
graph.bfs("a")