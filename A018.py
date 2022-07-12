#A018 보물
'''
a b받고 b의 크기순서 알아내서 반대로 배치
b 못바꾸니까 그냥 크고 작은거 찾아서 곱하고 없애주기
'''

import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

S = 0
for i in range(N):
    S +=  min(A)*max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(S)
