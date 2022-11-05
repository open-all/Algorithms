class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        e = collections.defaultdict(list)

        for i, x in enumerate(parent):
            if x == -1:
                continue
            if s[i] == s[x]:
                continue

            e[i].append(x)
            e[x].append(i)

        N = len(parent)
        seen = [False] * N

        #deepest, longest... paths! (context lol)

        # longest -> combining two longest children paths and make them go
        # through this node to deepest using recursion
        def go(index, parent):
            seen[index] = True
            best = 1
            deepest = 1
            longest = []
            for c in e[index]:
                if c != parent:
                    r = go(c, index)

                    deepest = max(deepest, r[0] + 1)
                    longest.append(r[0])
                    best = max(best, r[1])

            # sorting is optional, you can keep track of the top 2 with more
            # if statements
            longest.sort(reverse=True)
            if len(longest) >= 2:
                best = max(best, longest[0] + longest[1] + 1)
            elif len(longest) >= 1:
                best = max(best, longest[0] + 1)
            return (deepest, best)

        best = 0
        for i in range(N):
            if not seen[i]:
                result = go(i, -1)
                best = max(best, result[1])

        # O(V+E) time and space optimal
        return best
