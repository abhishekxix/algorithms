import random


def hash(number):
  p = 10**9 + 7
  a = random.randint(1, p - 1)
  b = random.randint(0, p - 1)

  hash = (a * number + b) % p
  return hash


print('[', end=' ')
for i in range(10):
  print(hash(i), end=', ')
print(']')
