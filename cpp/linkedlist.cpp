#include <iostream>
#include <stack>

struct Node {
  int data;
  Node* next;

  Node(int data) {
    this->data = data;
    this->next = nullptr;
  }

  Node(int data, Node* next) {
    this->data = data;
    this->next = next;
  }
};

class CustomLinkedList {
 private:
  Node* head;
  Node* tail;
  int size;

 public:
  CustomLinkedList() {
    this->head = nullptr;
    this->tail = nullptr;
    this->size = 0;
  }

  CustomLinkedList(int data) {
    this->head = new Node(data);
    this->tail = this->head;
    this->size = 1;
  }

  ~CustomLinkedList() {
    std::stack<Node*> toDelete;
    Node* tmp = this->head;

    while (tmp) {
      toDelete.push(tmp);
      tmp = tmp->next;
    }

    while (!toDelete.empty()) {
      delete toDelete.top();
      this->size--;
      toDelete.pop();
    }
  }

  void pushBack(int data) {
    this->size++;

    if (!this->head) {
      this->head = this->tail = new Node(data);
      return;
    }

    this->tail->next = new Node(data);
    this->tail = this->tail->next;
  }

  void pushFront(int data) {
    this->size++;

    if (!this->head) {
      this->head = this->tail = new Node(data);
      return;
    }

    Node* tmp = new Node(data, this->head);
    this->head = tmp;
  }

  int popFront() {
    if (!this->head) return -1;

    this->size--;

    Node* tmp = this->head;
    this->head = this->head->next;
    int data = tmp->data;
    delete tmp;
    return data;
  }

  int popBack() {
    if (!this->head) return -1;

    this->size--;

    Node* tmp = this->head;

    while (tmp->next->next) {
      tmp = tmp->next;
    }

    tmp->next = nullptr;
    int data = this->tail->data;
    delete this->tail;
    this->tail = tmp;

    return data;
  }

  void insert(int pos, int data) {
    if (pos <= 0) return pushFront(data);

    if (pos >= size) return pushBack(data);

    this->size++;

    Node* tmp = this->head;

    while (pos-- > 1) {
      tmp = tmp->next;
    }

    Node* freshNode = new Node(data, tmp->next);
    tmp->next = freshNode;
  }

  int remove(int pos) {
    if (pos <= 0) return popFront();

    if (pos >= size - 1) return popBack();

    this->size--;

    Node* tmp = this->head;

    while (pos-- > 1) {
      tmp = tmp->next;
    }

    Node* nodeToDelete = tmp->next;
    tmp->next = nodeToDelete->next;
    int data = nodeToDelete->data;
    delete nodeToDelete;
    return data;
  }

  friend std::ostream& operator<<(std::ostream& os, const CustomLinkedList& ll);
};

std::ostream& operator<<(std::ostream& os, const CustomLinkedList& ll) {
  Node* tmp = ll.head;

  while (tmp) {
    os << tmp->data << " -> ";
    tmp = tmp->next;
  }
  os << "null\n";
  return os;
}

int main() {
  {
    CustomLinkedList ll;
    for (int i = 0; i < 4; i++) {
      ll.pushFront(i);
    }

    ll.popFront();
    ll.popBack();
    ll.insert(500, 10);
    ll.insert(-1, 69);
    ll.insert(2, 123);
    ll.remove(-1);
    ll.remove(500);
    ll.remove(1);

    std::cout << ll;
  }

  return 0;
}