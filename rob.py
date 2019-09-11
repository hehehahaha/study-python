#leecode 198
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        return dp[-1]
