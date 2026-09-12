class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1]*n
        sorted_indices = sorted(range(n), key = lambda x: arr[x])
        for i in sorted_indices:
            for x in range(1, d+1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break                
                dp[i] = max(dp[i], 1+dp[j])
            for x in range(1, d+1):
                j = i+x
                if j >= n or arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1+dp[j])
        return max(dp)