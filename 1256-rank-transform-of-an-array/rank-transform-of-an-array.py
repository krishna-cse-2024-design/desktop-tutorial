class Solution:
    def arrayRankTransform(self, arr):
        rank = {}

        # Sort unique values
        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i

        # Replace each element with its rank
        return [rank[num] for num in arr]