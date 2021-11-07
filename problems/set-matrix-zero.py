from typing import List


class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    rows = set()
    cols = set()

    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
          rows.add(i)
          cols.add(j)

    for rowIdx in rows:
      for i in range(len(matrix[rowIdx])):
        matrix[rowIdx][i] = 0

    for colIdx in cols:
      for i in range(len(matrix)):
        matrix[i][colIdx] = 0
