#A051

number = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

alpha = list(input())

result = 0

for i in alpha:
    for j in number:
        if i in j:
            result += number.index(j)+3

print(result)