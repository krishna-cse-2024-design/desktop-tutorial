class Solution:
    def smallestSubsequence(self, s: str) -> str:

        hs = defaultdict(int)
        prev = set()

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in hs:
                hs[s[i]] = i

        se = set()
        stack = []
        for i in range(len(s)):

            if s[i] in se: continue

            while stack and stack[-1] >= s[i] and i < hs[stack[-1]]:
                if stack[-1] in se:
                    se.remove(stack[-1])
                stack.pop()

            stack.append(s[i])
            se.add(s[i])

        
        return ("".join(stack))