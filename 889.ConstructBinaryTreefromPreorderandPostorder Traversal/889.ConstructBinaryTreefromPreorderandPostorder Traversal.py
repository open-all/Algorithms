class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        mapper = {}
        for i, v in enumerate(inorder):
            mapper[v] = i

        def recurse(low, high):
            #base case
            if low > high:
                return
            root = TreeNode(postorder.pop())
            mid = mapper[root.val]
            root.right = rec(mid+1,high)
            root.left = rec(low,mid-1)
            return root

        return rec(0,len(inorder)-1)
