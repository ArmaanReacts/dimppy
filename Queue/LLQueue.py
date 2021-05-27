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

if __name__ == "__main__":
    s = Queue(5)
    s.enqueue(1)
    s.enqueue(4)
    s.enqueue(2)
    s.enqueue(8)
    s.enqueue(6)
    print(len(s))
    print(s.isEmpty())
    print(s.isFull())
    s.enqueue(5)
    print(s.dequeue())
    print(s.first())
    s.display()
    print(s)
    s.clear()
    print(s)