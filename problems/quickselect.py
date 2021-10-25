import random


def partition(a, p, r):
  x = a[r]
  i = p - 1

  for j in range(p, r):
    if a[j] < x:
      i += 1
      a[i], a[j] = a[j], a[i]

  i += 1
  a[r], a[i] = a[i], a[r]
  return i


def random_partition(a, p, r):
  q = random.randint(p, r)
  a[q], a[r] = a[r], a[q]
  return partition(a, p, r)


def quickselect(a, p, r, i):
  if p == r:
    return a[p]
  q = random_partition(a, p, r)
  k = q - p + 1

  if k == i:
    return a[q]

  if i < k:
    return quickselect(a, p, q - 1, i)

  return quickselect(a, q + 1, r, i - k)


print(quickselect([12, 3, 5, 7, 19], 0, 4, 5))
