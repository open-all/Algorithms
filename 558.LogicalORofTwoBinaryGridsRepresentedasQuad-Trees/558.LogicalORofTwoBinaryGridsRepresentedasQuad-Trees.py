"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val | quadTree2.val, True)

        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and quadTree2.val):
            return Node(True, True)

        tl = self.intersect(quadTree1.topLeft or quadTree1, quadTree2.topLeft or quadTree2)
        tr = self.intersect(quadTree1.topRight or quadTree1, quadTree2.topRight or quadTree2)
        bl = self.intersect(quadTree1.bottomLeft or quadTree1, quadTree2.bottomLeft or quadTree2)
        br = self.intersect(quadTree1.bottomRight or quadTree1, quadTree2.bottomRight or quadTree2)

        kids = [tl, tr, bl, br]

        leaf_count = sum((k.isLeaf for k in kids))
        if leaf_count == len(kids):
            vals = set((k.val for k in kids))
            if len(vals) == 1:
                return Node(vals.pop(), True)

        return Node(False, False, tl, tr, bl, br)
