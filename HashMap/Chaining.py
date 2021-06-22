class _Node:
    __slots__ = '_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next
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
        if self.isEmpty():
            return "List is Empty!!"
        s = ''
        p = self._head
        while p:
            s = s+ str(p._element)+" "
            p = p._next
        return s
    # Check if list is empty
    def isEmpty(self):
        return self._size == 0

    # Add a node at end of the linkedlist
    def addLast(self,e):
        newest = _Node(e,None)
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    # Add a node at starting of linkedlist    
    def addFirst(self,e):
        newest = _Node(e,None)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
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
            newest = _Node(e,None)
            p = self._head
            i = 0
            while (i<position-1):
                p = p._next
                i += 1
            newest._next = p._next
            p._next = newest
            self._size += 1

    # Print the linkedlist
    def display(self):
        if self.isEmpty():
            # print("List is empty!")
            print()
            return
        p = self._head
        while p:
            print(p._element,end=" --> ")
            p = p._next
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
            print('List is empty!')
            return
        if self._size==1:
            e = self._head._element
            self._head=None
            self._tail=None
            self._size -= 1
            return e  
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e
    
    # Remove last node from the linked list
    def removeLast(self):
        if self.isEmpty():
            print('List is empty!')
            return
        elif (self._size==1):
            self.removeFirst()
            return
        p = self._head
        i = 1
        while(i<len(self)-1):
            p = p._next
            i += 1
        self._tail = p
        e = p._next._element
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

    def insertSorted(self,e):
        newest = _Node(e,None)
        if self.isEmpty():
            self._head = newest
        else:
            p = self._head
            q = self._head
            while p and p._element<e:
                q = p 
                p = p._next
            if p == self._head:
                newest._next = self._head
                self._head = newest 
            else:
                newest._next = q._next
                q._next = newest
        self._size += 1

class Hash():
    def __init__(self):
        self.hashSize = 10    
        self.hashTable = [0]* self.hashSize
        for i in range(self.hashSize):
            self.hashTable[i] = LinkedList()

    def hashCode(self,key):
        return key%self.hashSize

    def insert(self,e):
        i = self.hashCode(e)
        self.hashTable[i].insertSorted(e)

    def search(self,key):
        i = self.hashCode(key)
        return self.hashTable[i].search(key) != -1

    def display(self):
        for i in range(self.hashSize):
            print("[",i,"]",end = " ")
            self.hashTable[i].display()
        print() 

if __name__ == '__main__':
    H = Hash()
    H.insert(15)
    H.insert(92)
    H.insert(35)
    H.insert(56)
    H.insert(28)
    H.insert(12)
    H.insert(26)
    H.insert(46)
    H.display()
    print(H.search(35))
    print(H.search(36))