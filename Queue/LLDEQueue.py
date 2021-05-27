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
            return "DEQueue is Empty!"
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
    def addFirst(self,e):
        if self.isFull():
            print("DEQueue is Full!")
            return
        newest = _Node(e,None)
        if self.isEmpty():
            self._rare = newest
        else:
            newest._next = self._front
        self._front = newest
        self._size += 1
    def addLast(self,e):
        if self.isFull():
            print("DEQueue is Full!")
            return
        newest = _Node(e,None)
        if self.isEmpty():
            self._front = newest
        else:
            self._rare._next = newest
        self._rare = newest
        self._size += 1

    # Remove an element out of the Queue
    def removeFirst(self):
        if self.isEmpty():
            print("DEQueue is Empty!")
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
    def removeLast(self):
        if self.isEmpty():
            print('DEQueue is empty!')
            return
        elif (self._size==1):
            self.removeFirst()
            return
        p = self._front
        i = 1
        while(i<len(self)-1):
            p = p._next
            i += 1
        self._rare = p
        e = p._next._element
        self._rare._next = None    
        self._size -= 1
        return e
        
    # Return first or last  element of the Queue
    def first(self):
        if self.isEmpty():
            print("DEQueue is Empty!")
            return
        else:
            return self._front._element
    def last(self):
        if self.isEmpty():
            print("DEQueue is Empty!")
            return
        else:
            return self._rare._element

    # Display the Queue
    def display(self):
        if self.isEmpty():
            return "DEQueue is Empty!"
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