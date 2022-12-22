#include <iostream>

class Stack {
 private:
  size_t maxSize;
  size_t currSize;
  int* stack;

 public:
  Stack(size_t maxSize) {
    this->maxSize = maxSize;
    this->stack = new int[maxSize];
    this->currSize = 0;
  }

  ~Stack() { delete[] stack; }

  int push(int item) {
    if (this->currSize == this->maxSize) return -1;

    this->stack[this->currSize++] = item;
    return 0;
  }

  int pop() {
    if (this->currSize == 0) return -1;

    this->currSize--;
    return 0;
  }

  int top() {
    if (currSize == 0) return INT32_MIN;
    return stack[currSize - 1];
  }

  bool isEmpty() { return !currSize; }
};

class Queue {
 private:
  size_t maxSize;
  size_t currSize;
  int* queue;

 public:
  Queue(size_t maxSize) {
    this->maxSize = maxSize;
    this->queue = new int[this->maxSize];
    this->currSize = 0;
  }

  ~Queue() { delete[] queue; }

  int enqueue(int item) {
    if (currSize == maxSize) return -1;

    queue[currSize++] = item;
    return 0;
  }

  int dequeue() {
    if (currSize == 0) return -1;

    int tmp = queue[0];

    for (int i = 1; i < currSize; i++) {
      queue[i - 1] = queue[i];
    }

    currSize--;
    return tmp;
  }

  bool isEmpty() { return !currSize; }
};

int main() {
  Stack s(10);
  Queue q(10);

  for (int i = 0; i < 10; i++) {
    s.push(i);
    q.enqueue(i);
  }

  while (!s.isEmpty()) {
    std::cout << s.top() << " ";
    s.pop();
  }

  std::cout << std::endl;

  while (!q.isEmpty()) {
    std::cout << q.dequeue() << " ";
  }

  s.top();

  std::cout << std::endl;
  return 0;
}