class _Node:
    __slots__='_element','_next','_prev'
    def __init__(self,element,next,prev):
        self._element = element
        self._next = next
        self._prev = prev

class LinkedList:
    def __init__(self):
        self._head = None 
        self._tail = None
        self._size = 0

    # Size of linkedlist
    def __len__(self):
        return self._size
    # Print Queue using print function
    def __str__(self):
        self.display()
    # Check if list is empty
    def isEmpty(self):
        return self._size == 0

    # Add a node at end of the linkedlist
    def addLast(self,e):
        newest = _Node(e,None,None)
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
        self._tail = newest
        self._size += 1
    # Add a node at starting of linkedlist
    def addFirst(self,e):
        newest = _Node(e,None,None)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
        self._size += 1
    # Add a node at given index of linkedlist
    def addPos(self,e,position):  
        if position>self._size or position<0:
            return None 
        elif (position==0):
            self.addFirst(e)
        elif (position==len(self)):
            self.addLast(e)
        else:
            newest = _Node(e,None,None)
            p = self._head
            i = 0
            while (i<position-1):
                p = p._next
                i += 1
            newest._next = p._next
            newest._prev = p
            p._next._prev = newest
            p._next = newest
            self._size += 1
    
    # Print the linkedlist
    def display(self):
        if self.isEmpty():
            print("List is empty!")
            return
        p = self._head
        while p:
            print(p._element,end=" --> ")
            p = p._next
        print()

    # Print the linkedlist in reverse order
    def displayRev(self):
        if self.isEmpty():
            print("List is empty!")
            return
        p = self._tail
        while (p):
            print(p._element,end=" --> ")
            p = p._prev
        print()

    # Search for a key in the linkedlist. Returns the index
    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1

    # Remove first node from the linkedlist    
    def removeFirst(self):
        if self.isEmpty():
            print('List is Empty!!')
            return
        if self._size==1:
            e = self._head._element
            self._head=None
            self._tail=None
            self._size -= 1
            return e  
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1 
        return e 

    # Remove last node from the linked list
    def removeLast(self):
        if self.isEmpty():
            print("List is Empty!!")
            return
        elif (self._size==1):
            self.removeFirst()
            return
        e = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None 
        self._size -= 1
        return e 

    # Remove a node from a particular position
    def removePos(self,position):  
        if position == 0:
            self.removeFirst()
        elif position == len(self)-1:
            self.removeLast()
        elif position<0 or position>len(self)-1:
            print("Position out of range")
        else:
            p = self._head
            i = 0
            while (i<position-1):
                p = p._next
                i += 1
            e = p._next._element
            p._next = p._next._next
            p._next._prev = p
            self._size -= 1 
            return e
    # Remove node with a given value
    def removeVal(self,key):
        current = self._head
        prev = self._head
        if key == self._head._element:
            self.removeFirst()
            return
        elif key== self._tail._element:
            self.removeLast()
            return
        while current._next != None :
            if current._element == key:
                prev._next = current._next
                current._next._prev = prev
                self._size -= 1 
                return 
            else:
                prev = current
                current = current._next 
        print('Value not in list!')

    # Delete the entire linkedlist
    def clear(self):
        self._head = None 
        self._size = 0
        return "List is cleared!"

if __name__ == '__main__':
    L = LinkedList()
    L2 = LinkedList()
    L.addLast(7)
    L.addLast(4)
    L.addLast(8)
    L.addLast(1)
    L.addFirst(2)
    L.addLast(5)
    L.addLast(12)
    L.addPos(9,0)
    L.display()
    L.displayRev()

    L.removeVal(9)
    L.removeVal(12)
    L.removeVal(8)
    L.removeVal(14)
    L.display()
    

    
    x = L.removeFirst()
    print("Element Removed:",x)
    L.display()

    x = L.removeLast()
    print("Element Removed:",x)
    L.display()

    x = L.removePos(4)
    print("Element Removed:",x)
    L.display()
    L2.removeFirst()
    print(L.search(5))
    print(L.search(8))
    print("Size:",len(L))
    print(L.clear())
    L.display()