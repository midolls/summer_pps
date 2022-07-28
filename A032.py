#A032
# k층 n호에 살려면 아래층의 1호부터 b호고, 0층부터 i명,, 1층 2호면 0층의 1호2호 더한수 3명 2층2호면 이거 반복
t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    f = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            f[i] += f[i-1]
    print(f[-1])



