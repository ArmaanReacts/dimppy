class _Node:
    __slots__ = '_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next
    
class Stack:
    def __init__(self,N = 'inf'):
        self._top = None 
        self._N = N
        self._size = 0
    
    # Size of linkedlist
    def __len__(self):
        return self._size
    # Print stack using print function
    def __str__(self):
        if self.isEmpty():
            return "Stack is Empty!"
        s = ""
        p = self._top
        while p:
            s = str(p._element) + " "+s
            p = p._next
        return s
    # Check if list is empty
    def isEmpty(self):
        return self._size == 0
    # Check if stack is full
    def isFull(self):
        return self._size == self._N

    # Push an element to the stack
    def push(self,e):
        if self.isFull():
            print("Stack is Full!")
            return
        newest = _Node(e,None)
        if self.isEmpty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    # Pop an element out of the stack
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return
        elif self._size ==1:
            e = self._top._element
            self.clear()
            return e
        else:
            e = self._top._element
            self._top = self._top._next
            self._size -= 1
            return e
        
    # Return top element of the stack
    def top(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return
        else:
            return self._top._element

    # Display the Stack
    def display(self):
        if self.isEmpty():
            return "Stack is Empty!"
        s = ""
        p = self._top
        while p:
            s = "| "+str(p._element)+" " +s
            p = p._next
        print(s)
    
    # Delete the stack
    def clear(self):
        self._size = 0
        self._top = None

if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(4)
    s.push(2)
    s.push(8)
    s.push(6)
    print(len(s))
    print(s.isEmpty())
    print(s.isFull())
    s.push(5)
    print(s.pop())
    print(s.top())
    s.display()
    print(s)
    s.clear()
    print(s)