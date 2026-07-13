from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        digits = "123456789"
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(digits[start:start + length])

                if low <= num <= high:
                    ans.append(num)
        return ans
        