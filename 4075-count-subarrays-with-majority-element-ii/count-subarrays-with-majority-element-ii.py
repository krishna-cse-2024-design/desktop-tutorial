class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        bit = BIT(2 * n + 3)

        shift = n + 2
        prefix = shift

        bit.update(prefix, 1)

        ans = 0

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bit.query(prefix - 1)
            bit.update(prefix, 1)

        return ans