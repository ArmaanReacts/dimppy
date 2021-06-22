class Heap:
    def __init__(self):
        self._maxSize = 10 
        self._data = [-1] * self._maxSize
        self._cSize = 0   

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0 

    def insert(self,e):
        if self._cSize == self._maxSize-1:
            print("No space in the Heap")
            return    
        self._cSize += 1
        hi = self._cSize
        while hi>1 and e> self._data[hi//2]:
            self._data[hi] = self._data[hi//2]
            hi = hi//2    
        self._data[hi] = e     

    def max(self):
        if self._cSize == 0:
            print("Heap is Empty!")
            return     
        return self._data[1] 

    def delete(self):
        if self._cSize == 0:
            print("Heap is Empty!")
            return 
        e = self._data[1]
        self._data[1] = self._data[self._cSize]
        self._data[self._cSize] = -1
        self._cSize -= 1 
        i = 1
        j = i*2
        while j<self._cSize:
            if self._data[j] < self._data[j+1]:
                j += 1   
            if self._data[i] < self._data[j]:
                self._data[i],self._data[j] = self._data[j] ,self._data[i]
                i = j 
                j = i*2 
            else:
                break 
        return e
            
if __name__ == '__main__':
    s = Heap()
    s.insert(25)
    s.insert(20)
    s.insert(2)
    s.insert(14)
    s.insert(10)
    s.insert(20)
    s.insert(2)
    s.insert(40)
    s.insert(10)
    print(s._data)
    s.delete()
    print(s._data)
    s.delete()
    print(s._data)
        