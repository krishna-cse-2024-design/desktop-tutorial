class Solution:
    def findSubstring(self, s, words):
        from collections import Counter

        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        target = Counter(words)
        res = []

        for i in range(word_len):
            left = i
            count = 0
            window = Counter()

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in target:
                    window[word] += 1
                    count += 1

                    while window[word] > target[word]:
                        window[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1

                    if count == len(words):
                        res.append(left)
                else:
                    window.clear()
                    count = 0
                    left = j + word_len

        return res