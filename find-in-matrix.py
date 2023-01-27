class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][-1] < target:
                left = middle + 1
            elif matrix[middle][0] > target:
                right = middle - 1
            else:
                return self.binSearch(matrix[middle], target)
        return False


    def binSearch(self, li: List[int], target: int) -> bool:
        left = 0
        right = len(li) - 1
        while left <= right:
            middle = (left + right) // 2
            if li[middle] < target:
                left = middle + 1
            elif li[middle] > target:
                right = middle - 1
            else:
                return True
        return False
