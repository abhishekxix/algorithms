import random
from typing import List


def are_equal(s1: str, l1: int, h1: int, s2: str, l2: int, h2: int) -> bool:
  i = l1
  j = l2

  while i <= h1:
    if s1[i] != s2[j]:
      return False
    i += 1
    j += 1

  return True


def polyhash(string: str, l: int, h: int, p: int, x: int) -> int:
  hash = 0
  for i in range(l, h + 1):
    hash = hash % p + (ord(string[i]) * x ** i) % p
    hash %= p

  return hash


def precompute_hashes(text: str, pattern: str, p: int, x: int) -> List[int]:
  hashes = [0 for i in range(0, len(text) - len(pattern) + 1)]
  s = text[len(text) - len(pattern):]
  hashes[-1] = polyhash(s, 0, len(s) - 1, p, x)

  idx = len(hashes) - 2

  y = (x**len(pattern)) % p

  while idx >= 0:
    hashes[idx] = ((x * hashes[idx + 1]) % p + ord(text[idx]) -
                   (ord(text[idx + len(pattern)]) * y) % p) % p
    idx -= 1

  return hashes


def rabin_karp(text: str, pattern: str):
  p = 10**9 + 7
  x = random.randint(1, p - 1)
  result = []
  text_hashes = precompute_hashes(text, pattern, p, x)
  pattern_hash = polyhash(pattern, 0, len(pattern) - 1, p, x)

  for i in range(0, len(text) - len(pattern) + 1):
    if text_hashes[i] == pattern_hash and are_equal(text, i, i + len(pattern) - 1, pattern, 0, len(pattern) - 1):
      result.append(i)

  return result


text = 'abcbabcabhabc'
pattern = 'abc'

print(rabin_karp(text, pattern))
