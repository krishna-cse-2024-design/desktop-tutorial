class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        C = [0] * k
        for x in arr:
            C[x % k] += 1

        return C[0] % 2 == 0 and C[1:] == C[:0:-1]