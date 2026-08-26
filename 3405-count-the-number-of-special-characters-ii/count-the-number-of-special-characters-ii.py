class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = [-1] * 26
        first_upper = [float('inf')] * 26
        
        for i, ch in enumerate(word):
            if ch.islower():
                idx = ord(ch) - ord('a')
                last_lower[idx] = i
            else:  # uppercase
                idx = ord(ch) - ord('A')
                if first_upper[idx] == float('inf'):
                    first_upper[idx] = i
        
        count = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != float('inf') and last_lower[i] < first_upper[i]:
                count += 1
        return count