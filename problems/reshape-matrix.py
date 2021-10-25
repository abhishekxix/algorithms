from typing import List

class Solution:
  def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    result = List[List[int]]
    k = 0
    l = 0

    if len(mat) * len(mat[0]) != r * c:
      return mat

    for i in range(len(mat)):
      for j in range(len(mat[0])):
        result[k].append(mat[i][j])
        l += 1        
        if l == c:
          result.append([])
          l = 0
          k += 1
    
    return result
