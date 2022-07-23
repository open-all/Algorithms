# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.righ = None

class Solution:
    def distance(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(list)

        queue = collections.deque([root])

        while queue:
            #pre order traversal
            #convert the tree into a graph
            node = queue.popleft()

            if node.right:
                queue.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)

            if node.left:
                queue.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)

        #breadth first search
        queue = collections.deque([target])
        distance = 0
        visited = set()
        visited.add(target)
        result = []
        while queue and distance <= k:
        #breadth first search
            for _ in range(len(queue)):
                node = queue.popleft()
                if distance == k:
                    result.append(node.val)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            distance += 1

        return result
