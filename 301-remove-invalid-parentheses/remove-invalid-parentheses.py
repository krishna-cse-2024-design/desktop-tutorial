class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        
        currSet = set([s])
        ans = []

        while True:
            for ss in currSet:
                if isValid(ss):
                    ans.append(ss)
            if len(ans) > 0:
                return ans
            newSet = set()
            for ss in currSet:
                for i in range(len(ss)):
                    if i > 0 and ss[i] == ss[i - 1]:
                        continue
                    if ss[i] == '(' or ss[i] == ')':
                        newSet.add(ss[:i] + ss[i + 1:])
            currSet = newSet
        return ans
        