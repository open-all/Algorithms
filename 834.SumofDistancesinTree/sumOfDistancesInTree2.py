class Solution:
    def sumOfDistancesInTree(self, n, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n
        ans = [0] * n
        def dfs(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                ans[child] = ans[node] - count[child] + n - count[child]
                dfs2(child, node)

        dfs(0, None)
        dfs2(0, None)
        return ans
