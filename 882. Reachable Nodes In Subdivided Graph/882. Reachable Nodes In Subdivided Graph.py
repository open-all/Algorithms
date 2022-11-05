class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w+1))
            graph[v].append((u, w+1))

        dist = [sys.maxsize] * n
        dist[0] = 0

        pq = [(0,0)] # current distance to node u

        while pq:
            d, u = heappop(pq)

            for v, nd in graph[u]:
                if d + nd < dist[v]:
                    dist[v] = d + nd
                    heappush(pq, (d+nd, v))
        ans = 0

        for u, w in enumerate(dist):
            if dist[u] <= maxMoves:
                ans += 1

        for u, v, w in edges:
                if dist[u] > maxMoves and dist[v] > maxMoves:
                    continue

                cnt1 = max(maxMoves - dist[u], 0)
                cnt2 = max(maxMoves - dist[v], 0)

                ans += min(cnt1+cnt2, w)

        return ans
