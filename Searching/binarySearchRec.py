def search(arr,key,left,right):            
    if left>right:
        return -1
    else:
        mid = (left+right)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return search(arr,key,mid+1,right)
        elif arr[mid]>key:
            return search(arr,key,left,mid-1)

if __name__ == "__main__":
    a = eval(input('Array: '))
    a.sort()
    l = len(a)
    k = int(input('Search for: '))
    print("Found at:",search(a,k,0,l-1))