#include <bits/stdc++.h>

struct ListNode
{
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
  ListNode *removeNthFromEnd(ListNode *head, int n)
  {
    ListNode *fast;
    ListNode *temp;
    fast = head;
    int k = 0;

    while (fast != nullptr)
    {
      k += 1;
      fast = fast->next;
    }
    int j = k - n;
    int f = 1;
    fast = head;
    while (fast != nullptr)
    {
      if (f == j)
      {
        temp = fast->next;

        fast->next = temp->next;
        delete temp;

        return head;
      }
      else
      {
        fast = fast->next;
        f += 1;
      }
    }

    return head;
  }
};

int main()
{
  ListNode *head = new ListNode(1);
  ListNode *temp = head;
  for (int i = 2; i <= 5; i++)
  {
    temp->next = new ListNode(i);
    temp = temp->next;
  }
  Solution sol;
  sol.removeNthFromEnd(head, 2);

  return 0;
}