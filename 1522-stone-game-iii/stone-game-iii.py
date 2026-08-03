class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        DP = [-inf] * (n + 1)
        DP[-1] = 0

        for sp in range(n - 1, -1, -1):
            curr_lead = 0
            for ep in range(sp, sp + 3):
                if ep == n:
                    break
                curr_lead += stoneValue[ep]
                DP[sp] = max(DP[sp], curr_lead - DP[ep + 1])
        if DP[0] > 0:
            return 'Alice'
        return "Bob" if DP[0] else 'Tie'