class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows * columns - 1

        while left <= right:
            mid = (left + right) // 2
            row_mid = mid // columns
            col_mid = mid % columns

            if matrix[row_mid][col_mid] == target:
                return True
            elif matrix[row_mid][col_mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False