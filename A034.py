#A034
import sys
input = sys.stdin.readline

nums = []
for i in range(10):
    n = int(input())
    val = n%42
    nums.append(val)

cnt = set(nums)
cnt = list(cnt)

print(len(cnt))


