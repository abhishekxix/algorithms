from typing import List
import max_heap

def heapsort(arr: List[int]):
  heap_size = len(arr)
  max_heap.build_max_heap(arr)

  for i in range(len(arr) - 1, 0, -1):
    temp = arr[0]
    arr[0] = arr[i]
    arr[i] = temp
    heap_size -= 1
    max_heap.max_heapify_it(arr, heap_size, 0)


heapsort([6, 5, 4, 3, 2, 1])