class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = [node for node in graph.keys() if len(graph[node]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = set()
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.add(neighbor)

            leaves = new_leaves

        return leaves
