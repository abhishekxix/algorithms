import random
from typing import Pattern


def polyhash(str, i, j, p, x):
  hash = 0

  for idx in range(i, j + 1):
    hash = (hash + ord(str[idx]) * x**(idx)) % p

  return hash


def precompute_hashes(text: str, pattern: str, p: int, x: int):
  hash = [0 for idx in range(len(text) - len(pattern))]
  hash[-1] = polyhash(text, len(text) - len(pattern) - 1, len(text) - 1, p, x)

  i = len(hash) - 2
  y = x**len(pattern) % p

  while i >= 0:
    hash[i] = ((x * hash[i + 1]) + (ord(text[i]) -
               ord(text[i + len(pattern) - 1]) * y)) % p
    i -= 1

  return hash


def rabin_karp(text: str, pattern: str):
  p = 10**9 + 7
  x = random.randint(1, p - 1)
  result = []
  text_hashes = precompute_hashes(text, pattern, p, x)
  pattern_hash = polyhash(pattern, 0, len(pattern) - 1, p, x)

  for i in range(0, len(text) - len(pattern)):
    if text_hashes[i] == pattern_hash:
      result.append(i)

  return result


text = 'abcdbcdapqrabc'
pattern = 'abc'

print(rabin_karp(text, pattern))
