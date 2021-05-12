def linearSearch(arr,key):
    length = len(arr)
    index = 0
    while index<length:
        if arr[index]==key:
            return index 
        index += 1
    return -1

if __name__ == "__main__":
    a = eval(input('Array: '))
    k = int(input('Search for: '))
    print("Found at:",linearSearch(a,k))