from typing import List


class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def unpackLayer(
        matrix: List[List[int]],
        r: int,
        m: int,
        c: int,
        n: int,
        result: List[int]
    ):
      if r > m:
        m = r = len(matrix) // 2

      if c > n:
        n = c = len(matrix[0]) // 2

      for i in range(c, n + 1):
        result.append(matrix[r][i])

      for i in range(r + 1, m + 1):
        result.append(matrix[i][n])

      if r < m:
        for i in range(n - 1, c - 1, -1):
          result.append(matrix[m][i])

      if c < n:
        for i in range(m - 1, r, -1):
          result.append(matrix[i][c])

    result = []

    r = 0
    c = 0
    m = len(matrix) - 1
    n = len(matrix[0]) - 1

    while len(result) < len(matrix) * len(matrix[0]):
      unpackLayer(matrix, r, m, c, n, result)

      r += 1
      m -= 1
      c += 1
      n -= 1

    return result


print(Solution().spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))
