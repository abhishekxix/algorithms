from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    self.reverse(self, nums, 0, len(nums))
    self.reverse(self, nums, 0, k)
    self.reverse(self, nums,k, len(nums))
  

  def reverse(self, nums, l, h):
    h -= 1
    while l < h:
      temp = nums[l]
      nums[l] = nums[h]
      nums[h] = temp
      l += 1
      h -= 1



nums = [1,2,3,4,5,6,7]  

sol = Solution
sol.rotate(sol, nums, 3)