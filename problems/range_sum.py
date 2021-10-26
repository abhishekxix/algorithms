class NumArray:

  def __init__(self, nums: List[int]):
    self.prefix_array = [nums[0]]
    for i in range(len(nums) - 1):
      self.prefix_array.append(self.prefix_array[i] + nums[i + 1])

  def sumRange(self, left: int, right: int) -> int:
    return self.prefix_array[right] - self.prefix_array[left]
