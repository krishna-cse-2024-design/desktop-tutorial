from typing import List

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = 1 << 62
        row = [INF]*n
        row[0] = 1
        w0 = waitCost[0]
        for j in range(1, n):
            prev = row[j-1] + (0 if j == 1 else w0[j-1])
            row[j] = prev + (j+1)
        for i in range(1, m):
            wp = waitCost[i-1]
            wc = waitCost[i]
            nr = [INF]*n
            base = row[0] + (0 if i == 1 else wp[0])
            nr[0] = base + (i+1)
            for j in range(1, n):
                a = row[j] + wp[j]
                b = nr[j-1] + wc[j-1]
                nr[j] = (a if a < b else b) + (i+1)*(j+1)
            row = nr
        return row[n-1]