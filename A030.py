#A030 좋은날 싫은날
#같은 변수 사용해서 계산할때 업데이트 되는지 잘 확인

n,now = map(int,input().split())

gg,gb,bg,bb = map(float,input().split())

good = 0
bad = 0

if now == 0:
    good = gg
    bad = gb
else:
    good = bg
    bad = bb

for i in range(n-1):
    a = good
    b = bad
    good = (a*gg) + (b*bg)
    bad =  (a*gb) + (b*bb)

print(round(good*1000))
print(round(bad*1000))




