from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while i < j:
      other = target - numbers[i]

      while numbers[j] > other:
        j -= 1
      
      if other == numbers[j]:
        return [i + 1, j + 1]
      
      i += 1
    

sol = Solution()
sol.twoSum([2,7,11,15], 9)
