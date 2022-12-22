from typing import List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    indices = {}

    for i in range(len(nums)):
      if nums[i] not in indices:
        indices[nums[i]] = [i]
      else:
        indices[nums[i]].append(i)

    result = []

    for number in nums:
      i = indices[number][0]
      otherNumber = target - number
      if otherNumber in indices:
        for j in indices[otherNumber]:
          if j != i:
            return [i, j]

    return result


print(Solution().twoSum([2, 7, 11, 15], 9))
