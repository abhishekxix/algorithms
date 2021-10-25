from typing import Dict


class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    mp1 = [0 for i in range(26)]
    mp2 = [0 for i in range(26)]
    hs = set()

    for char in s1:
      mp1[ord(char) - ord('a')] += 1
      hs.add(char)

    
    contains_perm = False

    for i in range(len(s2)):
      if hs.__contains__(s2[i]):
        if mp2[ord(s2[i]) - ord('a')] < mp1[ord(s2[i]) - ord('a')]:
          mp2[ord(s2[i]) - ord('a')] += 1
      else:
        contains_perm = Solution.checkperm(mp1, mp2) 
        if contains_perm: return True
        mp2 = [0 for i in range(26)]

    return Solution.checkperm(mp1, mp2) 
    
  @staticmethod 
  def checkperm(a, b):
    for i in range(26):
      if a[i] != b[i]:
        return False
    
    return True


s1 = "adc"

s2 = "dcda"

sol = Solution()
sol.checkInclusion(s1, s2)
