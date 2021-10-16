import random


def polyhash(str, i, j):
  hash = 0
  p = 10**9 + 7
  x = random.randint(1, p - 1)

  for idx in range(i, j + 1):
    hash = (hash + ord(str[idx]) * x**idx) % p

  return hash


print(polyhash('abhishek singh', 0, len('abhishek singh') - 1))
