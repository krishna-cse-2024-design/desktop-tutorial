class Solution:
    def maxDepth(self, s: str) -> int:
        a, p=0, 0
        for c in s:
            p+=(c=='(')-(c==')')
            a=max(a, p)
        return a
        