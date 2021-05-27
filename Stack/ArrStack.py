class Stack:
    def __init__(self,N = 'inf'):
        self._data = [] 
        self._N = N  

    # Size of Stack
    def __len__(self):
        return len(self._data)
    # Print stack using print function
    def __str__(self):
        if self.isEmpty():
            return "Stack is Empty!"
        s = ""
        for i in self._data:
            s += str(i) + " "
        return s
    # Check if stack is empty
    def isEmpty(self):
        return len(self._data) == 0
    # Check if stack is full
    def isFull(self):
        return len(self._data) == self._N

    # Push an element to the stack
    def push(self,e):
        if self.isFull():
            print("Stack is Full!")
            return
        else:
            self._data.append(e)

    # Pop an element out of the stack
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return
        else:
            return self._data.pop()

    # Return top element of the stack
    def top(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return
        else:
            return self._data[-1]
    
    # Display the Stack
    def display(self):
        for i in self._data:
            print("|",i,end=" ")
        print()
    
    # Delete the stack
    def clear(self):
        self._data = []
    
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
