class Solution:
  def climbStairs(self, n: int) -> int:
    jumps = [0 for i in range(0, n + 1)]
    if n == 1:
      return 1
    jumps[0] = 1
    jumps[1] = 1

    i = 2
    while i <= n:
      jumps[i] = jumps[i - 1] + jumps[i - 2]
      i += 1

    return jumps[n]
