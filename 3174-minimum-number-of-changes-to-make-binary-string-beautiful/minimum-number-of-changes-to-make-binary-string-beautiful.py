class Solution:
    def minChanges(self, s: str) -> int:
        return sum(starmap(ne, batched(s, 2)))