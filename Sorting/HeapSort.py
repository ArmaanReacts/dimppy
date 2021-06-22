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

def sort(A):
    H = Heap()
    n = len(A)
    for i in range(n):
        H.insert(A[i])
    k = n-1 
    for i in range(H._cSize):
        A[k] = H.delete()
        k -= 1 

if __name__ == "__main__":
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)