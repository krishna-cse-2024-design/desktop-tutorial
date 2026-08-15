class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        j = 0
        count = 0
        for i in range(k):
            if s[i] in "aeiou":
                count += 1
        i = 0     
        max = count   
        for j in range(k,len(s)):
            if s[j] in "aeiou":
               count += 1
            if s[i] in "aeiou":
                count -= 1
            i += 1
            if count > max:
                max = count
        return max           