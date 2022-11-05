class Solution:
    # recusive greedy algorithm solution
    # 
    def checkWays(self, pairs: List[List[int]]) -> int:
        alist = collections.defaultdict(set)
        done = set()

        for x, y in pairs:
            alist[x].add(y)
            alist[y].add(x)

        def tryroot(curr):
            done.add(curr)
            curr_set = alist[curr]
            N = len(curr_set)
            consider = sorted([(len(alist[k]), k) for k in alist[curr]],reverse=True)

            for c, k in consider:
                alist[k].remove(curr)

            ans = 1
            processed = 1
            for entry, k in consider:
                if k in done:
                    continue
                if len(alist[k]) == N - 1:
                    ans = 2

                n,p = tryroot(k)
                processed += p
                # when we see 0 we know it's not possible so we return
                if n == 0:
                    return 0, processed
                if n == 2:
                    ans = 2

            if processed > N + 1:
                ans = 0
            return ans, processed

        for x in alist.keys():
            if len(alist[x]) + 1 == len(alist):
                return tryroot(x)[0]

        return 0
