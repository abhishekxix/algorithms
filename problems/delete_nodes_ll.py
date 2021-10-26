# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head == None:
      return head

    while head != None and head.val == val:
      head = head.next

    prev = head
    curr = head.next

    while curr != None:
      if curr.val == val:
        prev.next = curr.next
        curr = prev.next
      else:
        curr = curr.next
        prev = prev.next

    return head
