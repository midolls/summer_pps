class Solution:
    def getPrimaryNum_Eratos(N) :
        nums = [True] * (N + 1)

        for i in range(2, len(nums) // 2 + 1):
            if nums[i] == True:
                for j in range(i+i, N, i):
                    nums[j] = False
        return [i for i in range(2, N) if nums[i] == True]

    def countPrimes(self, n: int) -> int:
        prime_nums = Solution.getPrimaryNum_Eratos(n)

        return len(prime_nums)