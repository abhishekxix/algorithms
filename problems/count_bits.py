from typing import List


class Solution:
  def countBits(self, n: int) -> List[int]:
    count = [0]
    if n == 0:
      return count

    for i in range(1, n):
      if i % 2 == 0:
        count.append(count[i / 2])
      else:
        count.append(count[i - 1] + 1)

    return count
