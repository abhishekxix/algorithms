from typing import List


class Solution:

  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    l = 0
    h = len(letters) - 1

    while(l <= h):
      mid = l + (h - l) // 2
      if(letters[mid] == target):
        break

      if(target < letters[mid]):
        h = mid - 1
      else:
        l = mid + 1

    if(letters[mid] == target):
      while letters[mid] == target:
        mid += 1
        mid %= len(letters)

      return letters[(mid)]

    return letters[l % len(letters)]


sol = Solution()
print(sol.nextGreatestLetter(["c", "f", "j"], "j"))
