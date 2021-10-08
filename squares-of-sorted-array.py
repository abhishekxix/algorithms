from typing import List
 

class Solution:

  def sortedSquares(self, nums: List[int]) -> List[int]:
    l = 0
    r = len(nums) - 1
    k = r
    ans = [0 for i in range(0, len(nums))]
    nums = [abs(i) for i in nums]

    while l != r:
      if nums[l] == nums[r]:
        ans[k] = nums[r] * nums[r]
        l += 1
  
      elif nums[l] > nums[r]:
        ans[k] = nums[l]**2
        l += 1

      else:
        ans[k] = nums[r] ** 2
        r -= 1

      k -= 1
    ans[k] = nums[l]**2
    return ans

   
  


nums = [-7,-3,2,3,11]
sol = Solution()
sol.sortedSquares(nums)