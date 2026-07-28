class Solution:
    def smallestPalindrome(self, s: str) -> str:
        letter_counts = [0] * 26
        for ch in s:
            letter_counts[ord(ch) - ord("a")] += 1

        left_half = ""
        middle_char = ""

        for i in range(26):
            count = letter_counts[i]
            left_half += chr(ord("a") + i) * (count // 2)
            if count % 2 == 1:
                middle_char = chr(ord("a") + i)

        right_half = left_half[::-1]
        return left_half + middle_char + right_half