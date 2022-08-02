#A048

n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    err = 0
    for j in range(len(word)-1) :
        if  word[j] != word[j+1]:
            new_word = word[j+1:]
            if new_word.count(word[j])>0:
                err+=1
    if err ==0:
        cnt+=1

print(cnt)

