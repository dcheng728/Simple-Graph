import math
import numpy as np

class Node:
    def __init__(self,name = None):
        self.outEdges = [] #Edges that go from this node to others
        self.inEdges = []   #Edges that are to edges from other nodes
        self.neighbours = []
        self.name   = name
        
class Edge:
    def __init__(self,fromNode,toNode,weight = 0):
        """
        (From Node) --this edge--> (To Node)
        """
        self.fromNode = fromNode 
        self.toNode = toNode
        self.weight = weight
        fromNode.outEdges.append(self)
        toNode.inEdges.append(self)
        fromNode.neighbours.append(toNode)
        toNode.neighbours.append(fromNode)

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.directed = False
        
    class FoundNodeException(Exception):
        """
        Exception class to help with node search methods
        """
        pass
        
    def checkNeighbours(self,nodeA,nodeB):
        """
        returns: True if A and B are neighbours, False if A and B are neighbours
        """
        #Check if nodeA has an edge from nodeA to nodeB
        for outEdge in nodeA.outEdges:
            if outEdge.toNode == nodeB:
                return True
        #Check if nodeB has an edge from nodeB to nodeA
        for outEdge in nodeB.outEdges:
            if outEdge.toNode == nodeA:
                return True
        return False
    
    def addNode(self,name = None):
        """
        Add a new node in the graph
        """
        newNode = Node(name)
        self.nodes.append(newNode)
        return newNode
    
    def addEdge(self,fromNode,toNode,weight = 0):
        """
        Add an edge that connects two nodes
        """
        newEdge = Edge(fromNode,toNode,weight)
        self.edges.append(newEdge)
        return newEdge
    
    def removeEdge(self,edge):
        """
        Remove an edge E, say E connects A and B,
        if A and B are not neighbors after removing this edge:
            remove B from A.neighbours
            remove A from B.neighbours
        """
        edge.fromNode.outEdges.remove(edge)
        edge.toNode.inEdges.remove(edge)
        if (self.checkNeighbours(edge.fromNode,edge.toNode) == False):
            edge.fromNode.neighbours.remove(edge.toNode)
            edge.toNode.neighbours.remove(edge.fromNode)
        self.edges.remove(edge)
    
    def removeNode(self,nodeR):
        """
        Remove one node from the graph, and remove all edges connected to it or from it
        """
        for n in range(len(nodeR.inEdges)):
            self.removeEdge(nodeR.inEdges[0])
        for n in range(len(nodeR.outEdges)):
            self.removeEdge(nodeR.outEdges[0])
        self.nodes.remove(nodeR)
    
    def DFSRec(self,currentNode,targetNode,visitedNodes):
        """
        Recursion helper method of DFS Method
        """
        if (currentNode == targetNode):
            raise self.FoundNodeException
        else:
            visitedNodes.append(currentNode)
            if (self.directed == True):
                for outEdge in currentNode.outEdges:
                    if (outEdge.toNode not in visitedNodes):
                        self.DFSRec(outEdge.toNode,targetNode,visitedNodes)
            else:
                for node in currentNode.neighbours:
                    if (node not in visitedNodes):
                        self.DFSRec(node,targetNode,visitedNodes)
           
    def DFS(self,startNode,targetNode):
        """
        Performs the Depth first search algorithm with the DEFRec recursion helper method
        @startNode: The node to start with
        @targetNode: The node to search
        returns: True if a path exists, False if there is no path
        """
        try:
            self.DFSRec(startNode,targetNode,[])
            return False
        except self.FoundNodeException:
            return True
    
    def isConnected(self):
        """
        Checks whether the graph is connected.
        returns: True if connected, False if not connected
        """
        if len(self.edges) < (len(self.nodes)-1):
            return False
        else:
            for n in range(len(self.nodes)):
                for i in range(n+1,len(self.nodes)):
                    if (self.DFS(self.nodes[n],self.nodes[i])==False):
                        print(self.nodes[n].name)
                        print(self.nodes[i].name)
                        return False
            return True
    
    def copy(self):
        """
        copy the existing graph
        returns: an exact copy of this graph
        """
        newG = Graph()
        for node in self.nodes:
            newG.addNode(Node(node.name))
        for edge in self.edges:
            newG.addEdge(newG.nodes[self.nodes.index(edge.fromNode)],
                         newG.nodes[self.nodes.index(edge.toNode)],
                         edge.weight)
        newG.directed = self.directed
        return newG
        
    def getLeaves(self):
        """
        returns: a list of all nodes that are leaves in this graph
        """
        leaves = []
        for node in self.nodes:
            if len(node.neighbours) <= 1:
                leaves.append(node)
        return leaves
    
    def isCyclic(self):
        """
        Checks whether this graph is cyclic
        return: True if this graph is cyclic, False if this graph is acyclic
        """
        if len(self.nodes) == 0:
            return False #If this graph has no nodes it is acyclic
        else:
            newG = self.copy()
            while True:
                leaves = newG.getLeaves()
                if len(leaves) == 0:
                    break
                else:
                    for leaf in leaves:
                        newG.removeNode(leaf)
            print(len(newG.nodes))
            if len(newG.nodes) == 0:
                return False
            else:
                return True
            
    def isTree(self):
        """
        Checks whether this graph is a tree
        returns: True if it is a tree, False if it is not
        """
        if self.isConnected and len(self.edges) == len(self.nodes)-1:
            return True
        else:
            return False
            