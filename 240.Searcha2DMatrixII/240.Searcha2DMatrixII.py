class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        while(r < len(matrix) and c >= 0):
            if (matrix[r][c] == target):
                return True
            elif (matrix[r][c] < target):
                r += 1
            else:
                c -= 1
        return False
