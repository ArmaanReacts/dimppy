def sort(a,mode=0):
    if mode == 0:                                               # Ascending
        n = len(a)
        mx = max(a)
        digits = len(str(mx))
        l = []
        bins = [l]*10
        for i in range(digits):
            for j in range(n):
                e = int((a[j]/pow(10,i))%10)
                if len(bins[e])>0:
                    bins[e].append(a[j])
                else:
                    bins[e] = [a[j]]
            k = 0
            for x in range(10):
                if len(bins[x])>0:
                    for y in range(len(bins[x])):
                        a[k] = bins[x].pop()
                        k += 1
        return a     
    elif mode == 1:                                             # Descending
        n = len(a)
        mx = max(a)
        digits = len(str(mx))
        l = []
        bins = [l]*10
        for i in range(digits):
            for j in range(n):
                e = int((a[j]/pow(10,i))%10)
                if len(bins[e])>0:
                    bins[e].append(a[j])
                else:
                    bins[e] = [a[j]]
            k = n-1
            for x in range(10):
                if len(bins[x])>0:
                    for y in range(len(bins[x])):
                        a[k] = bins[x].pop()
                        k -= 1
        return a 

if __name__=='__main__':
    import time
    seconds_1 = time.time()
    a = [9,6,5,8,7,2,3,0,1,4]
    print(sort(a))
    print(sort(a,1))
    seconds = time.time()
    print("runtime:",seconds-seconds_1)