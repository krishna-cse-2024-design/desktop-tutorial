from typing import List
#edges = (k*(k - 1))/2 where k is nodes
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(graph[node])

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    n_nodes, n_edges = dfs(neighbor)
                    nodes += n_nodes
                    edge_count += n_edges

            return nodes, edge_count

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)

                # Each edge is counted twice
                edge_count //= 2

                if edge_count == nodes * (nodes - 1) // 2:
                    answer += 1

        return answer