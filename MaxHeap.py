import math

class MaxHeap:
  def __init__(self) -> None:
    self.heap_size = 0
    self.heap = [0 for i in range(10)]

  def left(self, i: int):
    return 2 * i + 1
  
  def right(self, i: int):
    return 2 * i + 2
  
  def parent(self, i: int):
    return i // 2

  def max_heapify(self, i: int):
    while True:
      l = self.left(i)
      r = self.right(i)
      largest = i
      
      if l < self.heap_size and self.heap[l] > self.heap[i]:
        largest = l

      if r < self.heap_size and self.heap[r] > self.heap[largest]:
        largest = r
      
      if largest != i:
        temp = self.heap[i]
        self.heap[i] = self.heap[largest]
        self.heap[largest] = temp
        i = largest
      
      else:
        return

  def heap_max(self):
    return self.heap[0]

  def heap_extract_max(self):
    if self.heap_size == 0:
      return None
    
    val = self.heap[0]
    temp = self.heap[0]
    self.heap[0] = self.heap[self.heap_size - 1]
    self.heap[self.heap_size - 1] = temp
    self.heap_size -= 1
    self.max_heapify(0)
    return val

  def heap_increase_key(self, i: int, key: int):
    if key < self.heap[i]:
      return None
    
    self.heap[i] = key

    while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
      temp = self.heap[self.parent(i)]
      self.heap[self.parent(i)] = self.heap[i]
      self.heap[i] = temp
      i = self.parent(i)

  def heap_insert_key(self, key: int):
    if len(self.heap) == self.heap_size:
      self.heap.extend([0 for i in range(0, len(self.heap) // 2)])
    
    self.heap[self.heap_size] = -math.inf
    self.heap_size += 1
    self.heap_increase_key(self.heap_size - 1, key)


heap = MaxHeap()
for i in range(10):
  heap.heap_insert_key(i)

while heap.heap_size:
  print(heap.heap_extract_max())