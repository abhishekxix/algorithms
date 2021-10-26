from typing import List


class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    n = len(nums)
    presence = [False for i in range(n + 1)]

    for number in nums:
      presence[number] = True

    result = []
    for i in range(1, n + 1):
      if not presence[i]:
        result.append(i)

    return result
