from typing import List


class Solution:
  def letterCasePermutation(self, s: str) -> List[str]:
    def buildPermutation(s, i, perm, curr, result):
      if i == len(s):
        result.append(perm)
        return

      perm += curr
      i += 1

      if (i < len(s) and s[i].isdigit()) or i == len(s):
        buildPermutation(s, i, perm, s[i]
                         if i < len(s) else '', result)
      else:
        buildPermutation(s, i, perm, s[i].upper()
                         if i < len(s) else '', result)
        buildPermutation(s, i, perm, s[i].lower()
                         if i < len(s) else '', result)

    result = []
    buildPermutation(s, -1, '', '', result)

    return result


print(Solution().letterCasePermutation(s="a1b2"))
