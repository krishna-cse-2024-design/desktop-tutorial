class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:

        n, mx = len(nums), max(nums)
        ans = mx + mx
        ctr = Counter()
        ctrs = [Counter()]
        
        twos = [num & - num for num in nums]
        nums = [num//two for num, two in zip(nums, twos)]
        for two in twos:
            ctr[two]+= 1
            ctrs.append(ctr.copy())

        for i in range(n):
            gcd_ , cnt, leastTwos = nums[i], 0, mx

            for j in range(i, n):
                gcd_ = gcd(gcd_, nums[j])

                c = ctrs[j+1] - ctrs[i]
                leastTwos, cnt = min(c.items(), default = (0,0)) 
                
                prod, length = gcd_ * leastTwos, (j - i + 1)    
                res = prod * length
                if cnt <= k:
                    res*= 2
                ans = max(ans, res)
                if 2 * prod * (n - i) <= ans:
                    break
        return ans    