from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        mid = 0

        while l <= h:
            mid = l + (h - l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                h = mid - 1

            else:
                l = mid + 1

        return l


nums = [int(num) for num in input().split(sep=' ')]
target = int(input('t:'))
sol = Solution()

print(sol.searchInsert(nums, target))
