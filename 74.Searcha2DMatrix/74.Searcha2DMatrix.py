class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #edge case, there is no matrix
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        #find value using binary search
        while left < right:
            mid = left + (right-left) // 2
            i = mid // n
            j = mid % n

            if marix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True

        return False
