class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums[0]
        max_ = nums[0]
        for i in range(1,n):
            if dp < 0:
                dp = nums[i]
            else:
                dp += nums[i]
            if dp > max_:
                max_ = dp
        return max_
