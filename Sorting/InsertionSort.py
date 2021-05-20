def sort(arr,mode=0):
    if mode==0:                                 # Ascending Order
        l = len(arr)
        for i in range(1,l):
            c = arr[i]
            p = i 
            while arr[p-1]>c and p>0:
                arr[p] = arr[p-1]  
                p = p-1
            a[p] = c
        return arr
    elif mode==1:                               # Descending Order
        l = len(arr)
        for i in range(1,l):
            c = arr[i]
            p = i 
            while arr[p-1]<c and p>0:
                arr[p] = arr[p-1]  
                p = p-1
            a[p] = c
        return arr
        
if __name__=='__main__':
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    print(sort(a,1))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)