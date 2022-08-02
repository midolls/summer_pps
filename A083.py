#A083 중복빼고 정렬

n = int(input())

num = list(map(int,input().split(" ")))
num = list(set(num))
num.sort()


print (*num)
