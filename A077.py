#A077

import sys

read = lambda: sys.stdin.readline().rstrip()

score = []
score_sort = []
answer = []
total = 0

for i in range(8):
    score.append(int(read()))

score_sort = sorted(score, reverse=True)
score_sort = score_sort[:5]

for i in score_sort:
    answer.append(score.index(i)+1)

answer.sort()
total = sum(score_sort)

print(total)
print(*answer)