from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def count_waviness(n):
            if n <= 0:
                return 0

            s = str(n)
            m = len(s)

            @lru_cache(None)
            def dp(idx, x, y, smaller, digit_num):
                if idx >= m:
                    return 0

                ans = 0

                if smaller:
                    for z in range(10):
                        if z == 0 and digit_num == 0:
                            ans += dp(idx + 1, y, z, True, 0)
                        elif digit_num >= 2 and (
                            (x > y and z > y) or
                            (x < y and z < y)
                        ):
                            ans += 10 ** (m - 1 - idx)
                            ans += dp(idx + 1, y, z, True, digit_num + 1)
                        else:
                            ans += dp(idx + 1, y, z, True, digit_num + 1)
                else:
                    upper = int(s[idx])

                    for z in range(upper + 1):
                        if z == 0 and digit_num == 0:
                            ans += dp(idx + 1, y, z, True, 0)

                        elif digit_num >= 2 and (
                            (x > y and z > y) or
                            (x < y and z < y)
                        ):
                            if z == upper:
                                remain = int(s[idx + 1:]) + 1 if idx + 1 < m else 1
                                ans += remain
                                ans += dp(idx + 1, y, z, False, digit_num + 1)
                            else:
                                ans += 10 ** (m - 1 - idx)
                                ans += dp(idx + 1, y, z, True, digit_num + 1)

                        else:
                            ans += dp(
                                idx + 1,
                                y,
                                z,
                                z < upper,
                                digit_num + 1
                            )

                return ans

            return dp(0, 0, 0, False, 0)

        return count_waviness(num2) - count_waviness(num1 - 1)