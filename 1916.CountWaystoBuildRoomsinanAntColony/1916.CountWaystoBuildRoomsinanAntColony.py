class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        # returns total ways to build tree with cur as root and the total node count of the subtree
        def dfs(cur):
            # base case
            if not graph[cur]:
                return 1, 1

            ways = 1
            # base count because 0 factorial would be 1
            curNodeCount = 0
            for child in graph[cur]:
                subTreeWays, subTreeNodeCount = dfs(child)
                combinations = (fact[curNodeCount + subTreeNodeCount] *
                                 invFact[curNodeCount] * invFact[subTreeNodeCount]) % mod
                ways = (ways * subTreeWays * combinations) % mod

                curNodeCount += subTreeNodeCount

            return ways, curNodeCount + 1

        # implement inverse factorial with modular
        mod = 10**9 + 7
        n = len(prevRoom)
        fact = [0] * n
        fact[0] = 1
        invFact = [0] * n
        invFact[0] = pow(1, mod - 2, mod)

        for i in range(1, n):
            fact[i] = (i * fact[i - 1]) % mod
            invFact[i] = pow(fact[i], mod - 2, mod)

        graph = defaultdict(list)

        for cur, pre in enumerate(prevRoom):
            graph[pre].append(cur)

        return dfs(0)[0]
