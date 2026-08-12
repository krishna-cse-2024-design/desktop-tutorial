class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        left = 0
        maxi = 0
        seen = defaultdict(int)
        n = len(nums)
        for right in range(n):
            seen[nums[right]] += 1
            while seen[nums[right]] > k:
                seen[nums[left]] -= 1
                if seen[nums[left]] == 0:
                    del seen[nums[left]]
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
        