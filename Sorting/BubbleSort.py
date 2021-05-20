def sort(arr,mode=0):
    if mode==0:                                                 # Ascending Order
        l = len(arr)
        for i in range(0,l-1):
            swap = False
            for j in range(0,l-1):  
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
                    swap = True
            if swap == False:
                break
        return arr
    elif mode==1:                                               # Descending Order
        l = len(arr)
        for i in range(0,l-1):
            swap = False
            for j in range(0,l-1):  
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
                    swap = True
            if swap == False:
                break
        return arr
        
if __name__=='__main__':
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    print(sort(a,1))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)