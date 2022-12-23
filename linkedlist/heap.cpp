#include <iostream>
#include <queue>

class Heap {
 private:
  size_t maxSize;
  size_t currSize;
  std::vector<int> heap;

  int leftChild(int idx) { return (idx * 2) + 1; }

  int rightChild(int idx) { return (idx * 2) + 2; }

  int parent(int idx) { return (idx - 1) / 2; }

  void bubbleUp(int idx) {
    while (heap[parent(idx)] > heap[idx]) {
      std::swap(heap[idx], heap[parent(idx)]);
      idx = parent(idx);
    }
  }

  void bubbleDown(int idx) {
    while ((idx < (currSize / 2)) and (leftChild(idx) < currSize and
                                       heap[leftChild(idx)] < heap[idx]) or
           (rightChild(idx) < currSize and heap[rightChild(idx)] < heap[idx])) {
      // idx is less than half of currSize and both children are internal and
      // either one or both of them are smaller than the idx element

      // both children are smaller than heap[idx]
      if (heap[leftChild(idx)] < heap[idx] and
          heap[rightChild(idx)] < heap[idx]) {
        // swap with left child if left child is smaller or equal to the right
        // child
        if (heap[leftChild(idx)] <= heap[rightChild(idx)]) {
          std::swap(heap[idx], heap[leftChild(idx)]);
          idx = leftChild(idx);
        } else {  // swap with the right child otherwise
          std::swap(heap[idx], heap[rightChild(idx)]);
          idx = rightChild(idx);
        }
      } else if (heap[leftChild(idx)] < heap[idx]) {
        // swap with left child if only the left child is smaller
        std::swap(heap[idx], heap[leftChild(idx)]);
        idx = leftChild(idx);
      } else {
        // swap with the right child otherwise
        std::swap(heap[idx], heap[rightChild(idx)]);
        idx = rightChild(idx);
      }
    }
  }

 public:
  Heap(size_t maxSize) : heap(maxSize) {
    this->maxSize = maxSize;
    this->currSize = 0;
  }

  int push(int item) {
    if (currSize == maxSize) return INT32_MIN;
    if (currSize == 0) {
      heap[0] = item;
      currSize++;
      return 0;
    }

    heap[currSize] = item;
    bubbleUp(currSize++);
    return 0;
  }

  int pop() {
    if (!currSize) return INT32_MIN;

    int tmp = heap[0];
    std::swap(heap[0], heap[--currSize]);
    bubbleDown(0);
    return tmp;
  }

  bool isEmpty() { return !currSize; }
};

int main() {
  int n = 0;
  std::cout << "Enter the size of heap -> ";
  std::cin >> n;
  std::cout << "\n";

  Heap h(n);
  for (int i = n; i >= 0; i--) {
    h.push(i);
  }

  while (!h.isEmpty()) {
    std::cout << h.pop() << " ";
  }

  std::cout << std::endl;

  return 0;
}