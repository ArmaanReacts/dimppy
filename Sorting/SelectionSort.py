def sort(arr,mode=0):
    if mode==0:                     # Ascending Order
        l = len(arr)
        for i in range (0,l-1):
            s = i
            for j in range(i+1,l):
                if arr[j]<arr[s]:
                    s = j
            arr[i],arr[s] = arr[s],arr[i]
        return arr
    elif mode==1:                   # Descending Order
        l = len(arr)
        for i in range (0,l-1):
            s = i
            for j in range(i+1,l):
                if arr[j]>arr[s]:
                    s = j
            arr[i],arr[s] = arr[s],arr[i]
        return arr
        
if __name__=='__main__':
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    print(sort(a,1))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)