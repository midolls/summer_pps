#A001	Assign Cookies

'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        k=0
        num=0
        for i in s:
            while k < len(g):
                if g[k] <= i:
                    num = num+1
                    k=k+1

        return num
        '''
#성공

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = 0
        cookie_j = 0

        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

