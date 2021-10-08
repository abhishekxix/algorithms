from typing import List, Set

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    vals = {}

    for i in range(len(nums)):
      if vals.__contains__(nums[i]):
        vals[nums[i]].append(i)
      else:
        vals[nums[i]] = [i]
    
    ans = []

    for i in range(len(nums)):
      if vals.__contains__(target - nums[i]):
        for j in vals.get(target - nums[i]):
          if j != i:
            ans.extend([i, j])
            return ans

nums = [3,2,4]
s = 6
sol = Solution()
sol.twoSum(nums, s)