class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N

        for i in range(N):
            dp[i] = 1
            for j in range(i):
                if nums[j] >= nums[i]: continue
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

"""

"""