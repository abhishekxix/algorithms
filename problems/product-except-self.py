from typing import List


class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    cz = 0

    result = [0 for i in range(len(nums))]
    for i in nums:
      if i == 0:
        cz += 1

    if cz > 1:
      return result

    if cz == 1:
      prod = 1
      idx = 0

      for i in range(len(nums)):
        if nums[i] != 0:
          prod *= nums[i]
        else:
          idx = i

      result[idx] = prod
      return result

    left = 1
    right = 1

    for i in nums:
      right *= i

    for i in range(len(nums)):
      right /= nums[i]
      result[i] = left * right
      left *= nums[i]

    return result
