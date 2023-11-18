s = [1, 5, 6, 1, 7, 9, 3, 10, 66]


o = [0 for _ in range(max(s) + 1)]



for item in s:
    o[item] += 1

res = []

for i in range(len(o)):
    if o[i]:
        while o[i] > 0:
            res.append(i)
            o[i] -=1


print(res)