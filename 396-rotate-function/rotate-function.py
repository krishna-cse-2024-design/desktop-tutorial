class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        Sum, n, F=sum(nums), len(nums), sum(i*x for i, x in enumerate(nums))
        return max([F]+[F:=F+Sum-n*nums[~k] for k in range(n-1)])