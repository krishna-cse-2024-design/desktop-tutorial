class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # char -> last index
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1 # jump left past the duplicate

            seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len