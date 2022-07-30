# Definition for a binary tree node.
# class TreeNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

""" Each subtree can save its structure using pre-order traversal
    or post-order traversal, and then we save the resulting structure
    in a hash table so when we come across that tree structure
    twice, we can efficiently retrieve the results from the table
"""
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        m = collections.defaultdict(int)
        self.helper(root, m, res)
        return res

    def helper(self, root, m, res):
        if not root:
            return '#'
        path = str(root.val) + ',' + self.helper(root.left, m, res) + ',' + self.helper(root.right, m, res)
        if m[path] == 1:
            res.append(root)
        m[path] += 1
        return path
