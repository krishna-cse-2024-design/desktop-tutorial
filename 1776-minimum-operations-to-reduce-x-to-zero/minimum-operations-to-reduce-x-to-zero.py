class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total=sum(nums)
        target=total-x
        if target==0:return len(nums)
        elif target<0:return -1
        n=len(nums)
        currentSum=slow=maxLen=0
        for fast in range(n):
            currentSum+=nums[fast]
            while currentSum>target:
                currentSum-=nums[slow]
                slow+=1
            if currentSum==target:
                maxLen=max(maxLen, fast-slow+1)
        return n-maxLen if maxLen!=0 else -1