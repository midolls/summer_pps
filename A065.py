#A065 좌표정렬하기
N = int(input())

nums = []
for i in range(N):
    [a, b] = map(int, input().split())
    nums.append([a, b])

nums = sorted(nums)

for i in range(N):
    print(nums[i][0], nums[i][1])
출처: https://somjang.tistory.com/entry/BaeKJoon-11650번-좌표-정렬하기-Python [솜씨좋은장씨:티스토리]