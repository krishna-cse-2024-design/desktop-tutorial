class Solution:
    def myAtoi(self, s: str) -> int:
        # print([i for i in range(48,58)])
 

        int_str = ""
        p1,p2=0,0
        plus_ord = ord('+')
        minus_ord = ord('-')
        dot_ord = ord('.')
        allowed = list(range(48,58))
        allowed.extend([minus_ord, plus_ord])
        have_sign = False
        if not s:
            return 0
        for i, l in enumerate(s):
            if p1 != i and ord(l) not in range(48,58):
                break
            if ord(l) in [ord(' ')]:
                p1+=1
                p2+=1
                continue
            
            if ord(l) in allowed:
                p2+=1
        if p1 >= len(s) or ord(s[p1]) not in allowed:
            return 0
        if not s:
            return 0
            
        def to_int(temp):
            print(temp)
            sign = 1
            if temp[0] == '+':
                temp = temp[1:]
            elif temp[0] == '-':
                sign = -1
                temp = temp[1:]
            if temp:
                temp = int(temp) * sign
                if -(2**31) <= temp and temp <= 2**31-1:
                    return temp
                elif temp <0:
                    return -(2**31)
                else:
                    return 2**31-1
            return 0
        return to_int(s[p1:p2])
        