class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        def dfs(curr):
            if not visited[nums[curr]]:
                visited[nums[curr]] = True
                for child in trees[curr]:
                    dfs(child)

        n = len(nums)
        if 1 not in nums:
            return [1] * n

        trees = defaultdict(list)
        for i, p in enumerate(parents):
            trees[p].append(i)

        currNode = nums.index(1)
        visited = [False] * (max(nums) + 2)
        ans = [1] * n
        currMissingNum = 1

        while currNode != -1:
            # mark all the numbers for the subtree rooted at currNode
            dfs(currNode)
            # find first missing number for the current subtree
            while visited[currMissingNum]:
                currMissingNum += 1

            ans[currNode] = currMissingNum
            # move to the next parent
            currNode = parents[currNode]

        return ans
