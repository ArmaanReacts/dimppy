class Queue:
    def __init__(self,N = 'inf'):
        self._data = [] 
        self._N = N  

    # Size of Queue
    def __len__(self):
        return len(self._data)
    # Print Queue using print function
    def __str__(self):
        if self.isEmpty():
            return "DEQueue is Empty!"
        s = ""
        for i in self._data:
            s += str(i) + " "
        return s
    # Check if Queue is empty
    def isEmpty(self):
        return len(self._data) == 0
    # Check if Queue is full
    def isFull(self):
        return len(self._data) == self._N

    # Insert an element to the Queue
    def addFirst(self,e):
        if self.isFull():
            print("DEQueue is Full!")
            return
        else:
            self._data.insert(0,e)
    def addLast(self,e):
        if self.isFull():
            print("DEQueue is Full!")
            return
        else:
            self._data.append(e)

    # Remove an element out of the Queue
    def removeFirst(self):
        if self.isEmpty():
            print("DEQueue is Empty!")
            return
        else:
            return self._data.pop(0)
    def removeLast(self):
        if self.isEmpty():
            print("DEQueue is Empty!")
            return
        else:
            return self._data.pop()

    # Return first or last element of the Queue
    def first(self):
        if self.isEmpty():
            print("DEQueue is Empty!")
            return
        else:
            return self._data[0]
    def last(self):
        if self.isEmpty():
            print("DEQueue is Empty!")
            return
        else:
            return self._data[-1]
    
    # Display the Queue
    def display(self):
        for i in self._data:
            print(i,"|",end=" ")
        print()
    
    # Delete the Queue
    def clear(self):
        self._data = []
    
if __name__ == "__main__":
    s = Queue(8)
    s.addFirst(1)
    s.addLast(4)
    s.addLast(2)
    s.addFirst(3)
    s.addLast(8)
    s.addFirst(5)
    s.addLast(6)
    s.addFirst(9)
    print(len(s))
    print(s.isEmpty())
    print(s.isFull())
    s.addLast(5)
    s.display()
    print(s.removeFirst())
    s.display()
    print(s.removeLast())
    s.display()
    print(s.first())
    print(s.last())
    print(s)
    s.clear()
    print(s)
