class Hash():
    def __init__(self):
        self.hashSize = 10    
        self.hashTable = [0]* self.hashSize

    def hashCode(self,key):
        return key%self.hashSize

    def lProbe(self,e):
        i = self.hashCode(e)
        j = 0 
        while self.hashTable[(i+j)%self.hashSize] != 0:
            j += 1       
        return (i+j)%self.hashSize
    
    def insert(self,e):
        i = self.hashCode(e)
        if self.hashTable[i] == 0:
            self.hashTable[i] = e 
        else: 
            i = self.lProbe(e)
            self.hashTable[i] = e 
        
    def search(self,key):
        i = self.hashCode(key)
        j = 0
        while self.hashTable[(i+j)%self.hashSize] != key:
            if self.hashTable[(i+j)%self.hashSize] == 0:
                return False
            j += 1
        return True 
    
    def display(self):
        print(self.hashTable)

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