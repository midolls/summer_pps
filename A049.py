#A049 비밀번호 발음하기

while(1):
    str = input()
    if str == 'end':
        break
    a=0#모음
    b=0#자음
    check = True
    if str in [a,e,i,o,u]:
        continue
        for i in str:
            if i in [a,e,i,o,u]:
                a +=1
                b=0
                if a>=2:
                    check = False
            else:
                b+=1
                a=0
                if b>=3:
                    check = False
        if check == True:
            for j in range(len(str)):
                if str[j] == str[j+1]:
                    check = False
                    if str[j] == 'e' or str[j] == 'o'
                    check =False


    else:
        check = False


