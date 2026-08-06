class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for i in s.lower():
            if i.isalpha() or i.isdigit():
                st+=i
        return st==st[::-1]