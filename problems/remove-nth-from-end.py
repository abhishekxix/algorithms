from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    count = 0
    temp = head

    while temp != None:
      temp = temp.next
      count += 1
    
    temp = head
    to_delete = count - n - 1
    
    if to_delete == -1:
      head = head.next
      return head

    while to_delete > 0 and temp.next != None:
      to_delete -= 1
      temp = temp.next

    temp.next = temp.next.next
    return head