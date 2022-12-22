from typing import List


class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    def dfs(board, i, j, l, word):
      if l == len(word):
        return True

      if (
          i >= len(board) or i < 0
          or
          j >= len(board[i]) or j < 0
          or
          word[l] != board[i][j]
      ):
        return False

      tmp = board[i][j]
      board[i][j] = ''

      isFound = (
          dfs(board, i + 1, j, l + 1, word)
          or
          dfs(board, i - 1, j, l + 1, word)
          or
          dfs(board, i, j + 1, l + 1, word)
          or
          dfs(board, i, j - 1, l + 1, word)
      )

      board[i][j] = tmp
      return isFound

    for i in range(len(board)):
      for j in range(len(board[i])):
        if(board[i][j] == word[0] and dfs(board, i, j, 0, word)):
          return True

    return False


print(Solution().exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
