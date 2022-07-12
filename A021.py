#A021	플러그

import sys
input = sys.stdin.readline

N = int(input())
list=[]
for i in range(N):
    nums = list.append(int(input()))

cnt=0
for i in list:
    cnt += (i-1)


print (cnt+1)