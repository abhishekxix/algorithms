from typing import List


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    currSum = 0
    maxSoFar = nums[0]

    for number in nums:
      currSum += number
      if currSum > maxSoFar:
        maxSoFar = currSum
      if currSum < 0:
        currSum = 0

    return maxSoFar
