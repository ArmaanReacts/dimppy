def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position = position - 1
        A[position] = cvalue
def sort(A):
    n = len(A)
    maxElement = max(A)
    l = []
    buckets = [l] * 10
    for i in range(n):
        j = int(n * A[i] / (maxElement + 1) )
        if len(buckets[j]) == 0:
            buckets[j] = [A[i]]
        else:
            buckets[j].append(A[i])
    for i in range(10):
        insertionSort(buckets[i])
    k = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            A[k] = buckets[i].pop(0)
            k = k + 1
    return A
if __name__ == "__main__":
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)