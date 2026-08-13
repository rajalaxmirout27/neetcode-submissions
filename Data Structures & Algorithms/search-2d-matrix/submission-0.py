class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])


        start = 0
        end = rows - 1

        while start <= end:
            mid_row = start + (end - start) // 2

            if matrix[mid_row][0] <= target and matrix[mid_row][cols-1] >= target:
                break
            elif matrix[mid_row][0] > target:
                end = mid_row - 1
            else:
                start = mid_row + 1

        else:
            return False


        start = 0
        end = cols - 1

        while start <= end:
            mid = start + (end - start) // 2

            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False