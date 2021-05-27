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
            return "Queue is Empty!"
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
    def enqueue(self,e):
        if self.isFull():
            print("Queue is Full!")
            return
        else:
            self._data.append(e)

    # Remove an element out of the Queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        else:
            return self._data.pop(0)

    # Return first element of the Queue
    def first(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        else:
            return self._data[0]
    
    # Display the Queue
    def display(self):
        for i in self._data:
            print(i,"|",end=" ")
        print()
    
    # Delete the Queue
    def clear(self):
        self._data = []
    
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
