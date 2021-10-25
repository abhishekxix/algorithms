from typing import List

class Solution:
  def reverseWords(self, s: str) -> str:
    s = s.split(' ')

    result = ''

    for i in range(len(s)):
      result += ''.join(self.reverse(list(s[i])))
      if i == len(s) - 1:
        break
      result += ' '
    
    return result

  
  def reverse(self, s: List[str]):
    i = 0
    j = len(s) - 1

    while i < j:
      temp = s[i]
      s[i] = s[j]
      s[j] = temp
      i += 1
      j -= 1
    return s
    

sol = Solution()
sol.reverseWords("Let's take LeetCode contest")