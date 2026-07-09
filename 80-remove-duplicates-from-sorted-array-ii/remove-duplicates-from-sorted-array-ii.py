class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_counter = defaultdict(int)
        k = 0

        for n in nums:
            nums_counter[n] += 1
            if nums_counter[n] <= 2:
                nums[k] = n
                k += 1

        return k