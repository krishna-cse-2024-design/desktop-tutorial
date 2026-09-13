class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        # preserve the bits that cannot be changed by XOR with x
        A = (a >> n) << n
        B = (b >> n) << n
        # we want to make the 2 numbers as balanced as possible to yield a larger product
        for i in range(n - 1, -1 , -1):
            # look at each bit from right to left for a and b
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            # if both bits are equal, we can set both bits to 1 at that bit index for A and B
            if bit_a == bit_b:
                A |= (1 << i)
                B |= (1 << i)
            # if both bits are not equal, we can only make one of them 1, the other must be zero. 
            # hence, to balance the numbers, we give it to the smaller number
            else:
                if A < B:
                    A |= (1 << i)
                    B |= (0 << i)
                else:
                    A |= (0 << i)
                    B |= (1 << i)
        return (A * B) %  (10 ** 9 + 7)
        