# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        # find the root
        leaves = set()
        treeDict = {} #convert tree to tree dict for O(1) runtime removal 
        for tree in trees:
            treeDict[tree.val] = tree
            if tree.left:
                leaves.add(tree.left.val)
                  
            if tree.right:
                leaves.add(tree.right.val)
                
        root = None
        
        for tree in trees:
            if tree.val not in leaves:
                root = tree
                break
            
        if not root:
            return None

        curLeaves = {}
        if root.left:
            curLeaves[root.left.val] = (-sys.maxsize, root.val, root, 0) # low, high, parent node, leftOrRight
        if root.right:
            curLeaves[root.right.val] = (root.val, sys.maxsize, root, 1)

        del treeDict[root.val]

        while treeDict:
            #while the tree isn't empty we will try to merge, every time we find a merge we delete                      that subtree from the tree dictionary until the dictionary is empty
            findTree = False
            for leaf, (low, high, par, leftOrRight) in curLeaves.items():
                if leaf in treeDict:
                    newTree = treeDict[leaf]
                    del curLeaves[leaf]
    
                    if newTree.left:
                        if low < newTree.left.val < high and newTree.left.val not in curLeaves:
                            curLeaves[newTree.left.val] = (low, newTree.val, newTree, 0)
                        else:
                            return None
    
                    if newTree.right:
                        if low < newTree.right.val < high and newTree.right.val not in curLeaves:
                            curLeaves[newTree.right.val] = (newTree.val, high, newTree, 1)
                        else:
                            return None
        
                    # update parent node
                    if leftOrRight == 0:
                        par.left = newTree
                    else:
                        par.right = newTree
        
                    findTree = True
                    del treeDict[newTree.val]
                    break
    
            if not findTree:
                return None
                    
        return root