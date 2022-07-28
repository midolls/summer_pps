'''A003	Plus One
int로구성된 리스트는 join못하는듯'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str,digits))
        num = int(''.join(digits))
        num=num+1
        digit = list(map(str,str(num)))

        return (digit)