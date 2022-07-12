#A015	검증수

import sys
input = sys.stdin.readline

number = 0
numlist = list(map(str, input().split()))

for i in numlist:
    number += (int(i)**2)

print(number%10)
