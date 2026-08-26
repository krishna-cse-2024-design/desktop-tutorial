class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            q=min(nums)
            s=nums.index(q)
            nums[s]=nums[s]*multiplier
        return(nums)