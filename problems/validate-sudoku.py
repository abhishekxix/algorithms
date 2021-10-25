from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    is_present = [False for x in range(9)]

    for row in board:
      is_present = [False for x in range(9)]
      for element in row:
        if element != '.':
          element = int(element)
          if is_present[element - 1]:
            return False
          is_present[element - 1] = True
    
    for i in range(9):
      is_present = [False for x in range(9)]
      for j in range(9):
        element = board[j][i]
        if element != '.':
          element = int(element)
          if is_present[element - 1]:
            return False
          is_present[element - 1] = True

    r, c = 0, 0

    while True:
      is_present = [False for x in range(9)]
      for i in range(r, r + 3):
        for j in range(c, c + 3):
          element = board[i][j]
          if element != '.':
            element = int(element)
            if is_present[element - 1]:
              return False
            is_present[element - 1] = True
      
      c += 3
      if c == 9:
        r += 3

        if r == 9:
          break
        c = 0
        
    return True