def sort(arr,mode=0):
    if mode==0:                                                 # Ascending Order
        l = len(arr)
        gap = l//2
        while gap>0:
            i = gap
            while i<l:
                temp = arr[i]
                j = i-gap
                while j>=0 and arr[j]>temp:
                    arr[j+gap] = arr[j]
                    j = j-gap
                arr[j+gap] = temp
                i += 1
            gap //= 2
        return arr
    elif mode==1:                                               # Descending Order
        l = len(arr)
        gap = l//2
        while gap>0:
            i = gap
            while i<l:
                temp = arr[i]
                j = i-gap
                while j>=0 and arr[j]<temp:
                    arr[j+gap] = arr[j]
                    j = j-gap
                arr[j+gap] = temp
                i += 1
            gap //= 2
        return arr


if __name__=='__main__':
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    print(sort(a,1))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)
    