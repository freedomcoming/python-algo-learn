


a = [2,2,11,9,6,8,10]




for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j+1],a[j] = a[j],a[j+1]



print(a)