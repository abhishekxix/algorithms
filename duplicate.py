from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for num in nums:
            if count.__contains__(num):
                return True
            count[num] = 1
        return False
