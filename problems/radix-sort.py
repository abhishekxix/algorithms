def radix_sort(nums):
  m = 12345
  d = 0

  while m:
    d += 1
    m //= 10

  for i in range(d):
    nums = counting_sort(nums, i)

  return nums


def counting_sort(nums, exp):
  c = [0 for i in range(10)]
  div = 10 ** exp

  for num in nums:
    idx = (num // div) % 10
    c[idx] += 1

  for i in range(1, 10):
    c[i] += c[i - 1]

  result = [0 for i in range(len(nums))]

  for i in range(len(nums) - 1, -1, -1):
    idx = (nums[i] // div) % 10
    result[c[idx] - 1] = nums[i]
    c[idx] -= 1

  return result


print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
