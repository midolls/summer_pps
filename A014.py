#A014
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start_index = 0
        check = []
        for i in range(len(nums)):
            if  i+1 < len(nums) and nums[i]+1 == nums[i+1]:
                continue
            if start_index == i:
                check.append(str(nums[start_index]))
            else:
                check.append(str(nums[start_index])+"->"+ str(nums[i]))

            start_index = i+1

        return check
