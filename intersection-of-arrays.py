from typing import List

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: 
    result = []
    mp1 = {}
    mp2 = {}

    for i in nums1:
      if not mp1.__contains__(i):
        mp1[i] = 1
      
      else:
        mp1[i] += 1
      
    for j in  nums2:
      if not mp2.__contains__(j):
        mp2[j] = 1
      
      else:
        mp2[j] += 1
    
    for k in mp1.keys():
      if mp2.__contains__(k):
        n = 0
        if mp1[k] == mp2[k]:
          n = mp1[k]
        else:
          n = min(mp1[k], mp2[k])

        for i in range(n):
          result.append(k)
    
    return result