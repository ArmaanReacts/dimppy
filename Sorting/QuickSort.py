def sort(a,low,high,mode=0):
    if low<high:
        p = partition(a,low,high,mode)
        sort(a,low,p-1,mode)
        sort(a,p+1,high,mode)
    return a

def partition(a,low,high,mode):
    pivot = a[low]
    i,j = low+1,high
    if mode == 0:                                               # Ascending
        while True:
            while i<=j and a[i]<=pivot:
                i += 1
            while i<=j and a[j]>=pivot:
                j -= 1
            if i<=j:
                a[i],a[j] = a[j],a[i]
            else:
                break
        a[low],a[j] = a[j],a[low]
        return j  
    elif mode == 1:                                             # Descending
        while True:
            while i<=j and a[i]>=pivot:
                i += 1
            while i<=j and a[j]<=pivot:
                j -= 1
            if i<=j:
                a[i],a[j] = a[j],a[i]
            else:
                break
        a[low],a[j] = a[j],a[low]
        return j 

if __name__=='__main__':
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a,0,len(a)-1))
    print(sort(a,0,len(a)-1,1))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)