from typing import List


class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longestStreak = 0

    for num in nums:
      if not (num - 1) in numSet:
        currentNum = num
        currentStreak = 1

        while (currentNum + 1) in numSet:
          currentNum += 1
          currentStreak += 1

        longestStreak = max(longestStreak, currentStreak)

    return longestStreak
