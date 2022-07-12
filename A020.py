#A020	지능형 기차
import sys
input = sys.stdin.readline

in_person = 0
max = 0

for i in range(4):
    a,b = map(int,input().split())
    in_person= in_person-a
    if max < in_person :
        max = in_person
    in_person= in_person+b
    if max < in_person :
        max = in_person
print(max)