import random

def partition(a, p, r):
  x = a[r]
  i = p - 1

  for j in range(p, r):
    if a[j] <= x:
      i += 1
      a[i], a[j] = a[j], a[i]
  
  a[i + 1], a[r] = a[r], a[i + 1]
  return i + 1

def random_partition(a, p, r):
  q = random.randint(p, r)
  a[q], a[r] = a[r], a[q]
  return partition(a, p, r)

def random_quicksort(a, p, r):
  if p < r:
    q = random_partition(a, p, r)
    random_quicksort(a, p, q - 1)
    random_quicksort(a, q + 1, r)


nums = [random.randint(0, 10) for i in range(10)]
print(nums)
random_quicksort(nums, 0, len(nums) - 1)
print(nums)