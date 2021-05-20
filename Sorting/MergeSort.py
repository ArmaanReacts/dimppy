def merge(s1,s2,s,mode):
    i = j = 0
    if mode==0:
        while i+j<len(s):
            if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
                s[i+j]=s1[i]
                i += 1
            else:
                s[i+j]=s2[j]
                j += 1
    elif mode==1:
        while i+j<len(s):
            if j==len(s2) or (i<len(s1) and s1[i]>s2[j]):
                s[i+j]=s1[i]
                i += 1
            else:
                s[i+j]=s2[j]
                j += 1        
def sort(s,mode=0):
    n = len(s)
    if n<2:
        return
    mid = n//2
    s1 = s[0:mid]
    s2 = s[mid:n]
    sort(s1,mode)
    sort(s2,mode)
    merge(s1,s2,s,mode)
    return s


if __name__=='__main__':
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    print(sort(a,1))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)
    
'''
    i,j,k = left,mid+1,left  
    B = [0]*(right+1)
    while i<=mid and j<=right:
        if mode==0:                                 # Ascending
            if A[i]<A[j]:
                B[k] = A[i]
                i += 1
            else:
                B[k] = A[j] 
                j += 1
            k += 1 
        elif mode==1:                               # Descending 
            if A[i]>A[j]:
                B[k] = A[i]
                i += 1
            else:
                B[k] = A[j] 
                j += 1
            k += 1
    while i<=mid:
        B[k] = A[i]       
        i += 1
        k += 1
    while j<=right:
        B[k] = A[j]
        j += 1
        k += 1
    for m in range(left,right+1):
        A[m] = B[m]
def sort(arr,left,right,mode=0):
    if left<right:
        mid = (left+right)//2
        sort(arr,left,mid,mode)
        sort(arr,mid+1,right,mode)
        merge(arr,left,mid,right,mode)
    return arr'''