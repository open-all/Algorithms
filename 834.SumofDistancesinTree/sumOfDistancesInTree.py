class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        # parent_sum - closer_nodes + further_nodes

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        closer_nodes_count = [0] * N
        ans = [0] * N
        seen = set()
        def dfs(cur):
            nonlocal closer_nodes_count, ans
            closer_nodes = 1

            for child in graph[cur]:
                if child not in seen:
                    seen.add(child)
                    child_nodes_count = dfs(child)
                    closer_nodes += child_nodes_count
                    ans[0] += child_nodes_count

            closer_nodes_count[cur] = closer_nodes

            return closer_nodes

        seen.add(0)
        dfs(0) # populate closer_nodes_count and ans[0]

        def dfs2(cur):
            nonlocal ans
            for child in graph[cur]:
                if child not in seen:
                    seen.add(child)
                    ans[child] = ans[cur] - closer_nodes_count[child] + (N - closer_nodes_count[child])
                    dfs2(child) #recursive function call

        seen = set()
        seen.add(0)
        dfs2(0) # using ans[0] as base to populate all the eother nodes' answer

        return ans
