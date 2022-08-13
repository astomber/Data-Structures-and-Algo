""" 
Graph 

........     +---------+     +-----+
: Bonn : --> | Berlin  | ..> | Ulm |
:......:     +---------+     +-----+
               H
               H train
               v
             +---------+
             | Koblenz |
             +---------+

Vertices (vertes): Nodes of the grap such as the city names above
Edge: The edge is the line that connects the pairs of vertices

Types of Graphs:

    **Weights can be negative or positive**
-Unweighted: Graph that contains no weight such as the edges don't have units or specified values about the length between each nodes.
-Weighted: Graph that contains weight. Such as edges have units or distances between each vertices (nodes)

-Undirected graph: Edges of the graph do not have a directions associated with them 
-directed graph: Edges of the graph have directions assoiated with them. Such as arrows

-cyclic graph: a graph that has at least one loop
-Acyclic graph: a graph with no loops. 
-Tree graph: is a special case of a directed acyclic graph


Use cases: Great for finding shortest path like directions

Adjacency Matrix: Square matrix such as a 2d array. Draws out all the edge connections to each verticies

 Ex:          A B C 
            A 0 0 0
            B 0 0 0
            C 0 0 0
"""

"""
class Graph:
    #creating a dictionary , keys will be the edges  
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)  #adding a vertex as the value, and then appending each edge as a key


 #values are the vertices (nodes), keys are each edge
customDict = {  "a" : ["b","c"],
                "b" : ["a", "d", "e"],
                "c" : ["a", "e"],
                "d" : ["b", "e", "f"],
                "e" : ["d", "f", "c"],
                "f" : ["d", "e"]
               }

graph = Graph(customDict)

graph.addEdge("e", "c")   #adding a vertex, edge

print(graph.gdict)



"""

#implementaiton with an adjacency list,



class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys(): #if a vertex doesnt exists aka empty dictionary, were searching in keys. Edge case
            self.adjacency_list[vertex] = []  # initializing our vertex (node), so EX: A: []
            return True
        return False  #if a vertex exists just skip

  
    
    def print_graph(self):
        for vertex in self.adjacency_list:      #looping in adjacency list
            print(vertex, ":", self.adjacency_list[vertex])   #vertex with a : then the index
    
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():  #edge casing if both vertexes exsist or not
            self.adjacency_list[vertex1].append(vertex2)   # vertex  ex: A--->B
            self.adjacency_list[vertex2].append(vertex1)   # vertex  ex: B--->A
            return True
        return False
    
    def remove_edge(self,vertex1,vertex2):
         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():      #edge casing if both vertexes exsist or not
            try:
                self.adjacency_list[vertex1].remove(vertex2) #.remove python built in
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:                               #try catch to remove value error
                print("\n Edge between", vertex1 ," and ",vertex2,"doesn't exist")
                pass
            return True
            
         return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys(): #edge casing if vertex exists
            for other_vertex in self.adjacency_list[vertex]:  #finds the other vertex linked to the vertex were removing
                self.adjacency_list[other_vertex].remove(vertex)     #removes the vertex existance in other vertex dict keys
            del self.adjacency_list[vertex]
            return True
        return False





custom_graph = Graph()  #instance of the graph class, creating a new object

custom_graph.add_vertex("A") #Vertex A
custom_graph.add_vertex("B") #Vertex B

custom_graph.add_edge("A","B")  #A and B are connected by an edge

custom_graph.print_graph()

preGraph = custom_graph
afterGraph = custom_graph

print("\n")
print("The pre graph before edge deletion \n")

preGraph.print_graph()

print("\n After removing the edge between A-B")
afterGraph.remove_edge("A","B")
print("\n")

afterGraph.print_graph()

afterGraph.remove_edge("A","B")


new_graph = Graph()

new_graph.add_vertex("A") #Vertex A
new_graph.add_vertex("B") #Vertex B
new_graph.add_vertex("C") #Vertex B
new_graph.add_vertex("D") #Vertex B


new_graph.add_edge("A","B") 
new_graph.add_edge("A","C") 
new_graph.add_edge("A","D") 
new_graph.add_edge("B","C") 
new_graph.add_edge("C","D") 

print("\n Pre graph before vertex deletion: ")

new_graph.print_graph()

print("\n Pre graph after vertex deletion of vertex D: \n")

new_graph.remove_vertex("D")
new_graph.print_graph()