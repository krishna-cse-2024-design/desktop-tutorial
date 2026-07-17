from typing import List
from collections import Counter
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = Counter(nums)

        cnt_g = [0] * (mx + 1) # cnt_g[g] = #pairs with gcd exactly g

        for g in range(mx, 0, -1):
            v = 0
            # count numbers divisible by g
            for mult in range(g, mx + 1, g):
                v += freq[mult]
                # inclusion-exclusion: remove pairs with larger gcd
                cnt_g[g] -= cnt_g[mult]
            cnt_g[g] += v * (v - 1) // 2

        pref = list(accumulate(cnt_g)) # pref[i] = #pairs with gcd <= i

        return [bisect_right(pref, q) for q in queries]