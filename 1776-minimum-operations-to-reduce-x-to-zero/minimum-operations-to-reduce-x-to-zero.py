class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        L = 0
        rS = 0
        maxLen = -1
        
        for R in range(len(nums)):
            rS += nums[R]
            
            while L < len(nums) and rS > target:
                rS -= nums[L]
                L += 1
            
            if rS == target:
                maxLen = max(R - L + 1, maxLen)
        
        return len(nums) - maxLen if maxLen != -1 else maxLen
            
        