class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    chars = set()

    i = 0
    j = 1

    if s == '': return 0

    chars.add(s[0])
    longest = 1

    while j < len(s):
      if not chars.__contains__(s[j]):
        chars.add(s[j])
      else:
        while s[i] != s[j]:
          chars.remove(s[i])
          i += 1
        i += 1
        

      longest = max(longest, j - i + 1)
      j += 1

      

    return longest



sol = Solution()
print(sol.lengthOfLongestSubstring("dvdf"))