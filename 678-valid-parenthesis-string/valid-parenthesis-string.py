class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        n = len(s)
        for i in range(n):
            if s[i]=='(':
                left.append(i)
            elif s[i]=='*':
                star.append(i)
            elif s[i]==')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star and left[-1]<star[-1]:
            left.pop()
            star.pop()
        if len(left)>0:
            return False
        return True