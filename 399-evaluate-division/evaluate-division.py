class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)

        for (u, v), val in zip(equations, values):
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = val
            graph[v][u] = 1 / val

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j] if i != j else 1

        answers = []

        for u, v in queries:
            answers.append(graph[u].get(v, -1))

        return answers