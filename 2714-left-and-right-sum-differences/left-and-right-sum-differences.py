from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left_sum = 0
        right_sum = sum(nums)

        for i in range(n):
            right_sum -= nums[i]
            ans[i] = abs(left_sum - right_sum)
            left_sum += nums[i]

        return ans