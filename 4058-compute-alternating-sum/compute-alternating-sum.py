class Solution:
    def alternatingSum(self, nums: List[int], ans = 0) -> int:

        for i in range(0, len(nums), 2): ans+= nums[i]
        for i in range(1, len(nums), 2): ans-= nums[i]
        return ans