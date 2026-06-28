class Solution:
    def isNumber(self, s: str) -> bool:
        digit = False
        dot = False
        exp = False

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                digit = True
                
            elif ch in "eE":
                if not digit or exp:
                    return False
                exp = True
                digit = False
                
            elif ch == ".":
                if dot or exp:
                    return False
                dot = True
                
            elif ch in "+-":
                if i > 0 and s[i-1] not in "eE":
                    return False
                    
            else:
                return False
                
        return digit