def binarySearch(arr,key):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            right = mid -1
        elif arr[mid]<key:
            left = mid +1 
    return -1

if __name__ == "__main__":
    a = eval(input('Array: '))
    a.sort()
    k = int(input('Search for: '))
    print("Found at:",binarySearch(a,k))