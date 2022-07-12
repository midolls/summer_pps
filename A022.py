#A022	핸드폰 요금

N = input()
t_list = list(map(int,input().split()))
Y = 0
M = 0

for time in t_list:
    Y += (int(time/30)+1)*10
    M += (int(time/60)+1)*15

if Y > M:
    print('M',M)
elif Y <M:
    print('Y',Y)
else:
    print('Y M',Y)