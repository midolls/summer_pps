#A006	문자열 내 p와 y의 개수

def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    for i in s:
        if i == 'P' or i == 'p':
            p_count+=1
        elif i == 'Y' or i == 'y':
            y_count+=1
    if p_count == y_count:
        return answer
    else:
        answer = False
        return answer