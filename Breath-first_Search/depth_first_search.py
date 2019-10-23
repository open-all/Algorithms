class Node:
    #constructor of node object
    def __init__(self, name):
        self.children = []
        self.name = name
    #adds a child to the node it is called on
    def addChild(self, name):
        self.children.append(Node(name))

    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
