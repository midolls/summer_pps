#A047
str = input()
list = []
cnt=0
for i in str:
    list.append(i)
    cnt+=1
    if cnt%10 == 0:
        cnt = 0
        print(''.join(list))
        list.clear()
print(''.join(list))