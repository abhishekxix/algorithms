from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 1

    while i <= len(nums) - 1 and j < len(nums):
      if j <= i:
        j = i + 1

      while j < len(nums) and nums[j] == 0:
        j += 1
      
      if nums[i] == 0 and j < len(nums):
        nums[i] = nums[j]
        nums[j] = 0
      i += 1

sol = Solution()
sol.moveZeroes([4,2,4,0,0,3,0,5,1,0])