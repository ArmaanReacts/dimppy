import numpy as np
class _Node:
    __slots__ = '_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next  
class Queue:
    def __init__(self,N = 'inf'):
        self._front = None 
        self._rare = None 
        self._N = N
        self._size = 0
    
    # Size of linkedlist
    def __len__(self):
        return self._size
    # Print Queue using print function
    def __str__(self):
        if self.isEmpty():
            return "Queue is Empty!"
        s = ""
        p = self._front
        while p:
            s += str(p._element) + " "
            p = p._next
        return s
    # Check if list is empty
    def isEmpty(self):
        return self._size == 0
    # Check if Queue is full
    def isFull(self):
        return self._size == self._N

    # Insert an element to the Queue
    def enqueue(self,e):
        if self.isFull():
            print("Queue is Full!")
            return
        newest = _Node(e,None)
        if self.isEmpty():
            self._front = newest
        else:
            self._rare._next = newest
        self._rare = newest
        self._size += 1

    # Remove an element out of the Queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        elif self._size ==1:
            e = self._front._element
            self.clear()
            return e
        else:
            e = self._front._element
            self._front = self._front._next
            self._size -= 1
            return e
        
    # Return first element of the Queue
    def first(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        else:
            return self._front._element

    # Display the Queue
    def display(self):
        if self.isEmpty():
            return "Queue is Empty!"
        s = ""
        p = self._front
        while p:
            s += str(p._element)+" | "
            p = p._next
        print(s)
    
    # Delete the Queue
    def clear(self):
        self._size = 0
        self._front = None
class Graph:
    def __init__(self,vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices,vertices))
        self._visited = [0] * vertices

    def insertEdge(self,u,v,x=1):
        self._adjMat[u][v] = x   

    def removeEdge(self,u,v):
        self._adjMat[u][v] = 0

    def existEdge(self,u,v):
        return self._adjMat[u][v] != 0 

    def vertexCount(self):
        return self._vertices

    def edgeCount(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        return count   

    def vertices(self):
        for i in range(self._vertices):
            print(i,end=" ")
        print()  

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i,"--",j)

    def outDegree(self,v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                 count += 1
        return count 

    def inDegree(self,v):
        count = 0 
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count += 1
        return count   

    def display(self):
        print(self._adjMat)

    def BFS(self,s):
        i = s
        q = Queue()
        visited = [0] * self._vertices
        print(i,end=' ')
        visited[i] = 1
        q.enqueue(i)
        while not q.isEmpty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j,end=' ')
                    visited[j] = 1
                    q.enqueue(j)
    def DFS(self,s):
        if self._visited[s]==0:
            print(s,end=' ')
            self._visited[s]=1
            for j in range(self._vertices):
                if self._adjMat[s][j]==1 and self._visited[j]==0:
                    self.DFS(j)

if __name__ == '__main__':
    # Unweighted Undirected
    G = Graph(4)
    G.display()
    print(G.vertexCount())
    print(G.edgeCount())
    G.insertEdge(0,1)
    G.insertEdge(1,0)
    G.insertEdge(0,2)
    G.insertEdge(2,0)
    G.insertEdge(1,2)
    G.insertEdge(2,1)
    G.insertEdge(3,2)
    G.insertEdge(2,3)
    G.display()
    print(G.vertexCount())
    print("Edges:",G.edgeCount())
    print("Out Degree:",G.outDegree(2))
    print("In Degree",G.inDegree(2))
    G.edges()
    print(G.existEdge(1,3))
    G.removeEdge(1,2)
    G.edges()
    print("Edges:",G.edgeCount())
    print(G.existEdge(1,2))

    # Weighted Undirected
    G = Graph(4)
    G.display()
    print(G.vertexCount())
    print(G.edgeCount())
    G.insertEdge(0,1,26)
    G.insertEdge(1,0,26)
    G.insertEdge(0,2,16)
    G.insertEdge(2,0,16)
    G.insertEdge(1,2,12)
    G.insertEdge(2,1,12)
    G.insertEdge(3,2,8)
    G.insertEdge(2,3,8)
    G.display()
    print(G.vertexCount())
    print("Edges:",G.edgeCount())
    print("Out Degree:",G.outDegree(2))
    print("In Degree",G.inDegree(2))
    G.edges()
    print(G.existEdge(1,3))
    G.removeEdge(1,2)
    G.edges()
    print("Edges:",G.edgeCount())
    print(G.existEdge(1,2))

    # Unweighted Directed
    G = Graph(4)
    G.display()
    print(G.vertexCount())
    print(G.edgeCount())
    G.insertEdge(0,1)
    G.insertEdge(0,2)
    G.insertEdge(1,2)
    G.insertEdge(2,3)
    G.display()
    print(G.vertexCount())
    print("Edges:",G.edgeCount())
    print("Out Degree:",G.outDegree(2))
    print("In Degree",G.inDegree(2))
    G.edges()
    print(G.existEdge(1,3))
    G.removeEdge(1,2)
    G.edges()
    print("Edges:",G.edgeCount())
    print(G.existEdge(1,2))

    # Weighted Directed
    G = Graph(4)
    G.display()
    print(G.vertexCount())
    print(G.edgeCount())
    G.insertEdge(0,1,26)
    G.insertEdge(0,2,16)
    G.insertEdge(1,2,12)
    G.insertEdge(2,3,8)
    G.display()
    print(G.vertexCount())
    print("Edges:",G.edgeCount())
    print("Out Degree:",G.outDegree(2))
    print("In Degree",G.inDegree(2))
    G.edges()
    print(G.existEdge(1,3))
    G.removeEdge(1,2)
    G.edges()
    print("Edges:",G.edgeCount())
    print(G.existEdge(1,2))
    print(G.BFS(0))
    print(G.DFS(0))