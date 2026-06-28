from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_len = 0

            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            num_words = j - i
            spaces = maxWidth - line_len

            # Last line or only one word
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                space_between = spaces // (num_words - 1)
                extra = spaces % (num_words - 1)

                line = ""
                for k in range(num_words - 1):
                    line += words[i + k]
                    line += " " * (space_between + (1 if k < extra else 0))
                line += words[j - 1]

            res.append(line)
            i = j

        return res