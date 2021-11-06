from typing import List


class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    result = [0 for i in range(len(nums))]

    k = len(nums) - 1
    i = 0
    j = len(nums) - 1

    while i <= j:
      if abs(nums[i]) > abs(nums[j]):
        result[k] = nums[i] ** 2
        i += 1
      else:
        result[k] = nums[j] ** 2
        j -= 1
      k -= 1

    return result
