class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        mp = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        ans = ['']

        for d in digits:
            temp = []
            for s in ans:
                for ch in mp[d]:
                    temp.append(s + ch)
            ans = temp

        return ans