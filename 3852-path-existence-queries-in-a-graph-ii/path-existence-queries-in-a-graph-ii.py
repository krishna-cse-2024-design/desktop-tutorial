from typing import List
import math

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        arr = sorted((v, i) for i, v in enumerate(nums))
        values = [x[0] for x in arr]

        # original index -> sorted position
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        LOG = n.bit_length() + 1

        jump = [[0] * LOG for _ in range(n)]

        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            jump[l][0] = r

        for k in range(1, LOG):
            for i in range(n):
                jump[i][k] = jump[jump[i][k - 1]][k - 1]

        def min_jump(start, end):
            if start == end:
                return 0

            if jump[start][0] >= end:
                return 1

            if jump[start][LOG - 1] < end:
                return math.inf

            ans = 0

            for k in range(LOG - 1, -1, -1):
                if jump[start][k] < end:
                    ans += 1 << k
                    start = jump[start][k]

            return ans + 1

        res = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            d = min_jump(a, b)

            if d == math.inf:
                res.append(-1)
            else:
                res.append(d)

        return res