class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:

    def process(original):
      modified = ''
      bsp = '#'
      j = len(original) - 1
      cnt = 0

      while j >= 0:
        while j >= 0 and original[j] == bsp:
          cnt += 1
          j -= 1

        while j >= 0 and original[j] != bsp and cnt:
          cnt -= 1
          j -= 1

        while j >= 0 and original[j] != bsp:
          modified += original[j]
          j -= 1

      return modified[::-1]

    sm = process(s)

    tm = process(t)

    return tm == sm


print(Solution().backspaceCompare("bxj##tw", "bxo#j##tw"))
