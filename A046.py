#A046
N = int(input())

list= sorted([input()[0] for _ in range(N)])

s = set(list)
res = []

for i in s:
    if list.count(i) >=5:
        res.append(i)

if len(res)>0:
    print("".join(sorted(res)))
else: print ("PREDAJA")