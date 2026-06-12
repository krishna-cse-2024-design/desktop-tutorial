class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = (n + 1).bit_length()

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        parent = [[0] * (n + 1) for _ in range(LOG)]

        stack = [1]
        visited = [False] * (n + 1)
        visited[1] = True

        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u
                    stack.append(v)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                p = parent[k - 1][v]
                if p:
                    parent[k][v] = parent[k - 1][p]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            a = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[a]
            ans.append(pow(2, d - 1, MOD))

        return ans