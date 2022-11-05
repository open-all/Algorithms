class Solution:
    def minCost(self, maxtTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        @lru_cache(None)
        def dp(u, curTime):
            if u == n-1:
                return passingFees[n-1]

            ans = sys.maxsize

            for (y, t) in graph[u]:
                if curTime + t <= maxTime:
                    ans = min(ans, passingFees[u] + dp(v, curTime+t))

            return ans

        graph = defaultdict(list)

        for u, v, t in edges:
            graph[u].append((v,t))
            graph[v].append((u,t))

        n = len(passingFees)

        ans = dp(0,0)

        return ans if ans < sys.maxsize else -1
