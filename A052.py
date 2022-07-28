#A052

n = int(input())

for i in range(n):
    cnt=0
    sum=0
    str = input()
    for j in str:
        if cnt ==0 and j == "O":
            sum+=1
            cnt +=1
        elif cnt>0 and j =="O":
            cnt+=1
            sum += cnt
        elif j =='X':
            cnt=0
    print(sum)