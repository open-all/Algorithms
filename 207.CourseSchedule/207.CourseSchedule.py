class Solution:
    #python solution using depth first seach
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            # base case1
            if crs in visitSet:
                return False
            # base case 2
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
