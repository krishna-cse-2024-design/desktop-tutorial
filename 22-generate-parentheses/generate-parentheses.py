class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(cur, open_cnt, close_cnt):
            if len(cur) == 2 * n:
                res.append(cur)
                return

            if open_cnt < n:
                backtrack(cur + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(cur + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res