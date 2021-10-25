import random


def are_equal(s1, l1, h1, s2, l2):
  i = l1
  j = l2

  while i <= h1:
    if s1[i] != s2[j]:
      return False

    i += 1
    j += 1

  return True


def polyhash(s, p, x):
  hash = 0

  for i in range(len(s)):
    hash = (hash + ord(s[i]) * x**i) % p

  return hash


def precompute_hashes(text, p_len, p, x):
  hashes = [0 for idx in range(len(text) - p_len + 1)]
  y = (x ** p_len) % p
  s = text[len(text) - p_len:]
  hashes[-1] = polyhash(s, p, x)

  i = len(hashes) - 2

  while i >= 0:
    hashes[i] = (x * hashes[i + 1] + ord(text[i]) -
                 ord(text[i + p_len]) * y) % p
    i -= 1

  return hashes


def rabin_karp(text, pattern):
  p = 10**9 + 7
  x = random.randint(1, p - 1)
  p_hash = polyhash(pattern, p, x)
  t_hash = precompute_hashes(text, len(pattern), p, x)
  result = []

  for i in range(len(t_hash)):
    if p_hash == t_hash[i] and are_equal(text, i, i + len(pattern) - 1, pattern, 0):
      result.append(i)

  return result


text = 'abhiabhiabhi'
pattern = 'bhi'
print(rabin_karp(text, pattern))
