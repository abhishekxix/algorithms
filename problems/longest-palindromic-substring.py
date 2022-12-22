from typing import List


class Solution:
  dp = None

  def isPalindrome(s, l, h):

    mid = l + (h - l)//2

    for i in range(l, mid + 1):
      if s[i] != s[h - (i - l)]:
        return False

    return True

  def longestPalindrome(self, s: str) -> str:
    l = len(s) + 1
    dp = [[0 for i in range(l)] for i in range(l)]
    ll = 0
    lh = 0

    for i in range(1, l):
      length_this_time = 1
      for j in range(i, l):
        longest_so_far = max(dp[i-1][j], dp[i][j-1], dp[i-1][-1])
        tmp = j - i + 1
        if (
            (tmp > longest_so_far)
            and s[i - 1] == s[j - 1]
            and Solution.isPalindrome(s, i - 1, j - 1)
        ):
          length_this_time = j - i + 1

        if length_this_time > dp[i-1][j]:
          dp[i][j] = length_this_time
          if length_this_time > dp[i][j - 1] and length_this_time > dp[i-1][-1]:
            ll = i - 1
            lh = j - 1
        else:
          dp[i][j] = dp[i-1][j]

    return s[ll: lh + 1]


print(Solution().longestPalindrome("aaaa"))
