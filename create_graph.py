from Graph import *
import random
import cv2


G = Graph()

nodes  = {}
edges = []

nodeName = ["A","B","C","D","E","F","G","H","I","J"]

for n in range(10):
    nodes[nodeName[n]] = G.addNode(nodeName[n])
    
edge0 = G.addEdge(nodes["A"],nodes["G"],1)
edge1 = G.addEdge(nodes["A"],nodes["E"],2)
edge2 = G.addEdge(nodes["G"],nodes["C"],3)
edge3 = G.addEdge(nodes["C"],nodes["I"],4)
edge4 = G.addEdge(nodes["B"],nodes["H"],9)
edge5 = G.addEdge(nodes["H"],nodes["D"],11)
edge6 = G.addEdge(nodes["J"],nodes["F"],7)
edge7 = G.addEdge(nodes["F"],nodes["A"],8)
edge8 = G.addEdge(nodes["B"],nodes["A"],2)

G.DFS(nodes["A"],nodes["J"])
print(G.isConnected())



print(G.isTree())
