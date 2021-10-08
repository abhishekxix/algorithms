from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    triangle = [[] for i in range(numRows)]

    triangle[0].append(1)

    for i in range(1, numRows):
      for j in range(i + 1):
        if j == 0 or j == i:
          triangle[i].append(1)
        
        else:
          triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    
    return triangle


sol = Solution()
sol.generate(5)