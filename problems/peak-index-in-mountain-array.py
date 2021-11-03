import math
from typing import List


class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    idx = 0
    maxElem = -math.inf
    for i in range(len(arr)):
      if arr[i] > maxElem:
        maxElem = arr[i]
        idx = i

    return idx
