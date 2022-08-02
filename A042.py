#042 Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        t1=[]
        for i in s:
            if s1 and i == "#":
                s1.pop(-1)
            elif not s1 and i == "#":
                continue
            else:
                s1.append(i)
        for j in t:
            if t1 and j == "#":
                t1.pop(-1)
            elif not t1 and j == "#":
                continue
            else:
                t1.append(j)

        s = ''.join(s1)
        t = ''.join(t1)

        print(s,t)

        if s == t:
            return True
        else :
            return False
