#A040
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        cnt1=0
        cnt2=0

        for i in s1:
            if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                cnt1+=1

        for i in s2:
            if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                cnt2+=1

        if cnt1 == cnt2:
            return True
        else:
            return False