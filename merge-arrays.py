from typing import List

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      """
      Do not return anything, modify nums1 in-place instead.
      """
      i = 0
      j = 0
      
      nums1[m:] = [] 
      
      while i < len(nums1) and j < n:    
        if nums1[i] >= nums2[j]:
          nums1.insert(i, nums2[j])
          j += 1     
        i += 1
              
  
      while j < n:
        i += 1
        nums1.insert(i, nums2[j])
        j += 1 

sol = Solution()
nums1 = [1, 3, 6]
nums2 = [1, 2, 3, 4 ,5, 6, 7]
sol.merge(nums1, len(nums1), nums2, len(nums2) - 2)
print(nums1)