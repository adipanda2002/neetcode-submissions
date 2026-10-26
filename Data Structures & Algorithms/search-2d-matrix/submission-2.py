class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = 0
        endRow = len(matrix) - 1

        while startRow <= endRow:
            rowIndex = startRow + (endRow - startRow) // 2
            rowMin = matrix[rowIndex][0]
            rowMax = matrix[rowIndex][-1]

            if target == rowMin or target == rowMax:
                return True

            if target < rowMin:
                endRow = rowIndex - 1
            elif target > rowMax:
                startRow = rowIndex + 1
            else:
                return self.searchRow(matrix[rowIndex], target)

        return False

    def searchRow(self, row: List[int], target: int) -> bool:
        start = 0
        end = len(row) - 1

        while start <= end:
            i = start + (end - start) // 2
            if row[i] < target:
                start = i + 1
            elif row[i] > target:
                end = i - 1
            else:
                return True
        return False