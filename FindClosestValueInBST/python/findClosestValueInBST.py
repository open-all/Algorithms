""" Find Closest Value In Binary Search Tree

You are given a binary search tree data structure consisting of binary
search tree nodes. Each binary search tree node has an integer value stored
in a property called 'value' and two children nodes stored in properties
called 'left' and 'right,' respectively. A node is said to be a binary
search tree node if and only if it satisfies the binary search tree property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and both of its children nodes are either binary search tree nodes themselves
or None (null) values. You are also given a target interger value; write a
function that finds the closest value to that target value contained in the
binary search tree. Assume that there will only be one closest value.
"""

# Average: O(Log(n)) | O(Log(n))
# worst: O(n) time | O(n) space
def findClosestValueInBstRecursive(tree, target):
    #initialize infinity or max int value of language or root node in tree
    return findClosestValueInBstHelperRecursive(tree, target, float("inf"))

def findClosestValueInBstHelperRecursive(tree, target, closest):
    "recursive implementation of binary search"
    #base case of binary search
    if tree is None:
        return closest
    #update closest before traversing the tree
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelperRecursive(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelperRecursive(tree.right, target, closest)
    else:
        return closest

# Average: O(Log(n)) | O(1) space
# worst: O(n) time | O(1) space
def findClosestValueInBstIterative(tree, target):
    return findClosestValueInBstHelperIterative(tree, target, float("inf"))

def findClosestValueInBstHelperIterative(tree, target, closest):
    "iterative implementation of binary search"
    currentNode = tree
    while currentNode is not None:
        #update closest before traversing the tree
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
