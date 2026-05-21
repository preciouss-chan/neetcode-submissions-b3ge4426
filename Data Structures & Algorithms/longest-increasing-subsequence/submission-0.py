from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                LIS += 1
                continue

            else:
                idx = bisect_left(dp, nums[i])
                dp[idx] = nums[i]

        return LIS