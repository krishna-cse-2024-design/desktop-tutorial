class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k==len(nums):
            return max(nums)
        c=Counter(nums)
        ans=-1
        if k>1:
            if c[nums[0]]==1:
                ans=max(ans,nums[0])
            if c[nums[-1]]==1:
                ans=max(ans,nums[-1])
        else:
            for i in c:
                if c[i]==1:
                    ans=max(ans,i)
        return ans