#A039
'''왜안될깡
A = False
for i in range(1,num+1):
    if num/i == i:
return(A)
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num**0.5) * int(num**0.5) == num