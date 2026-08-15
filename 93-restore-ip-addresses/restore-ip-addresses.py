class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtrack(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    ans.append(".".join(parts))
                return

            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]

                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(j + 1, parts)
                parts.pop()

        backtrack(0, [])
        return ans