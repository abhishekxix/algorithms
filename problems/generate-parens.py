from typing import List


class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    def buildValidParenthesCombination(
        n: int, curr: str, result: List[str], numOpen: int, bal: int
    ):
      if len(curr) == 2*n:
        result.append(curr)
        return

      if numOpen > n:
        return

      if numOpen < n:
        buildValidParenthesCombination(
            n, curr + '(', result, numOpen + 1, bal + 1
        )

      if bal != 0:
        buildValidParenthesCombination(n, curr + ')', result, numOpen, bal - 1)

    result = []
    buildValidParenthesCombination(n, '', result, 0, 0)
    return result


print(Solution().generateParenthesis(3))
