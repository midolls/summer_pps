#A013	Single Number
'''
같은게 중복돼있는거 말고 한번만 나오는 수 찾기
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            k = nums.count(i)
            if k == 1:
                num = i
        return(num)