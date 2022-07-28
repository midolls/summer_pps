#A035	화성 수학
'''
겨울 방학에 달에 다녀온 상근이는 여름 방학 때는 화성에 갔다 올 예정이다. (3996번) 화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다. 따라서, 화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.
연산되는 수가 정수가 아닐수도 있음주의
'''
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    list1 = list(map(str,input().split()))
    sum = float(list1[0])
    for i in range(1,len(list1)):
        if list1[i] == '@':
            sum*=3
        elif list1[i] == '%':
            sum+=5
        elif list1[i] == '#':
            sum-=7
    print(format(sum,".2f"))


