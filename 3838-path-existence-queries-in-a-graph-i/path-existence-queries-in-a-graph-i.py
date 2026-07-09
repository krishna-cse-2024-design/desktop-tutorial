from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        group = [0] * n
        group_id = 0

        # Assign each node to a connected component
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group_id += 1
            group[i] = group_id

        # Answer each query
        ans = []
        for u, v in queries:
            ans.append(group[u] == group[v])

        return ans