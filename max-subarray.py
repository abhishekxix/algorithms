from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        sum_so_far = nums[0]

        n = len(nums)

        for i in range(n):
            curr_sum += nums[i]

            if curr_sum > sum_so_far:
                sum_so_far = curr_sum

            if curr_sum < 0:
                curr_sum = 0

        return sum_so_far
