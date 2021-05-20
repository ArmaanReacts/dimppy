def sort(a,mode=0):
    if mode == 0:                                               # Ascending
        n = len(a)
        mx = max(a)
        cArray = [0]*(mx+1)
        for i in range(n):
            cArray[a[i]] += 1
        i,j = 0,0
        while i<mx+1:
            if cArray[i]>0:
                a[j] = i
                j += 1
                cArray[i] -= 1
            else:
                i += 1
        return a     
    elif mode == 1:                                             # Descending
        n = len(a)
        mx = max(a)
        cArray = [0]*(mx+1)
        for i in range(n):
            cArray[a[i]] += 1
        i = mx
        j = 0
        while i>=0:
            if cArray[i]>0:
                a[j] = i
                j += 1
                cArray[i] -= 1
            else:
                i -= 1
        return a

if __name__=='__main__':
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    print(sort(a,1))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)