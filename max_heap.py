from typing import List

def left(i: int):
  return 2 * i + 1

def right(i: int):
  return 2 * i + 2


def max_heapify(arr: List[int], heap_size: int, i: int):
  l = left(i)
  r = right(i)
  largest = i

  if l < heap_size and  arr[l] > arr[i]:
    largest = l
  
  if r < heap_size and arr[r] > arr[largest]:
    largest = r
  
  if largest != i:
    temp = arr[largest]
    arr[largest] = arr[i]
    arr[i] = temp
    max_heapify(arr, heap_size, largest)


def max_heapify_it(arr: List[int], heap_size: int, i: int):
  
  largest = -1

  while True:
    l = left(i)
    r = right(i)
    if l < heap_size and arr[l] > arr[i]:
      largest = l
    else:
      largest = i

    if r < heap_size and arr[r] > arr[largest]:
      largest = r
    
    if largest != i:
      temp = arr[largest]
      arr[largest] = arr[i]
      arr[i] = temp
      i = largest
    else: 
      break


def build_max_heap(arr: List[int]):
  heap_size = len(arr)
  for i in range(heap_size//2 - 1, -1, -1):
    max_heapify_it(arr, heap_size,i)
  
  return arr

