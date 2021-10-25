from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and target > matrix[row][col]:
            row += 1

        if row == len(matrix):
            return False

        return Solution.binary_search(matrix[row], 0, col, target)

    @staticmethod
    def binary_search(nums: List[int], l, h, target):
        while l <= h:
            mid = l + (h - l) // 2

            if nums[mid] == target:
                return True

            if nums[mid] > target:
                h = mid - 1

            else:
                l = mid + 1

        return False
