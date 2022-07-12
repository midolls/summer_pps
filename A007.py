#A007	음계 판별하기

list1 = list(map(str, input().split()))

for i in list1:
    str = "".join(list1)
if str == "12345678":
    print("ascending")

elif str == "87654321":
    print("descending")

else:
    print("mixed")