from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        LOG = (n + 1).bit_length()

        st_max = [[0] * n for _ in range(LOG)]
        st_min = [[0] * n for _ in range(LOG)]

        for i, x in enumerate(nums):
            st_max[0][i] = x
            st_min[0][i] = x

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1
            for i in range(n - length + 1):
                st_max[j][i] = max(st_max[j - 1][i], st_max[j - 1][i + half])
                st_min[j][i] = min(st_min[j - 1][i], st_min[j - 1][i + half])
            j += 1

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        def value(l, r):
            p = lg[r - l + 1]
            mx = max(st_max[p][l], st_max[p][r - (1 << p) + 1])
            mn = min(st_min[p][l], st_min[p][r - (1 << p) + 1])
            return mx - mn

        heap = []
        for l in range(n):
            heapq.heappush(heap, (-value(l, n - 1), l, n - 1))

        ans = 0

        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            ans += -val
            if r > l:
                heapq.heappush(heap, (-value(l, r - 1), l, r - 1))

        return ans