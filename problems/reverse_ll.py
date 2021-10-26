from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
      return head
    tail = head
    curr = head.next

    while(curr != None):
      tail.next = curr.next
      curr.next = head
      head = curr
      curr = tail.next

    return head
