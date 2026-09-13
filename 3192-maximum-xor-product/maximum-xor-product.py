class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        mask = (1 << n) - 1

        A = a & ~mask
        B = b & ~mask

        for i in range(n - 1, -1, -1):
            bit = 1 << i

            if (a & bit) == (b & bit):
                A |= bit
                B |= bit
            elif A < B:
                A |= bit
            else:
                B |= bit
        
        return (A % MOD) * (B % MOD) % MOD