class Solution(object):
    def __init__(self):
        self.result = 0

    def longestPath(self, parent, s):
        children = [[] for _ in range(len(s))]
        for i, j in enumerate(parent):
            if j >= 0:
                children[j].append(i)

        def dfs(i):
            tmp = [0]
            for j in children[i]:
                cur = dfs(j)
                if s[i] != s[j]:
                    tmp.append(cur)
            tmp = heapq.nlargest(2, tmp)
            self.result = max(self.result, sum(tmp) + 1)
            return max(tmp) + 1
        dfs(0)
        return self.result
