class Node:
    def __init__(self, name):
        self.children []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def breathFirstSearch(self, array):
        #initialize the queue array with the first node in the tree
        queue = [self]
        #while the queue is not empty
        while len(queue) > 0:
            #set current to the first node in the queue
            current = queue.pop(0)
            #append the current node to the output array
            array.append(current.name)
            #search for any children of the curr node and append them to the queue
            for child in current.children:
                queue.append(child)
                
        #at this point you have a sorted array of nodes
        return array
