#A081 N번쨰큰수

n = int(input())
num=[]
max=[]

for i in range(n):
    max1=2
    max2=1
    max3=0
    num = list(map(int, input().split(" ")))

    for j in range(10):

        if num[j] > max1:
            max3 = max2
            max2 = max1
            max1 = num[j]
        elif num[j] > max2:
            max3 = max2
            max2 = num[j]
        elif num[j] > max3:
            max3 = num[j]
    print(max3)

