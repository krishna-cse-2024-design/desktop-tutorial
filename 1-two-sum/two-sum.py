class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = defaultdict(int)
        for i, n in enumerate(nums):
            counter[n] = i
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in counter and counter[complement] != i:
                return [i, counter[complement]]
                