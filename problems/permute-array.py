from typing import List


class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    def buildPermutations(nums, result, present=set(), curr=[], i=0):
      if i == len(nums):
        result.append(curr[:])
        return

      j = 0
      while j < len(nums):
        if j not in present:
          curr.append(nums[j])
          present.add(j)
          buildPermutations(nums, result, present, curr, i + 1)
          curr.pop()
          present.remove(j)
        j += 1

    result = []
    buildPermutations(nums, result)
    return result


print(Solution().permute([1, 2, 3]))
