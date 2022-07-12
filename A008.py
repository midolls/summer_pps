import sys
input = sys.stdin.readline
i=0
N = int(input())

'''for _ in range(N):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt +=1
    mean = cnt/nums[0]
    print("%0.3f%%" %(mean))'''

#성공
import sys
input = sys.stdin.readline
i=0
N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt +=1
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')