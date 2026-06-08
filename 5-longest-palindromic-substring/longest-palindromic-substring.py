class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1 # length of palindrome

        for i in range(len(s)):
            len1 = expand_around_center(i, i) # odd length palindromes: "aba"
            len2 = expand_around_center(i, i + 1) # even length palindromes: "abba"
            curr_max = max(len1, len2)

            if curr_max > max_len:
                max_len = curr_max
                start = i - (curr_max - 1) // 2

        return s[start:start + max_len]