class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in matrix:
            left, right = 0, len(i) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if i[mid] == target:
                    return True
                elif i[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return False
