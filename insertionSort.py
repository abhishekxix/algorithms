from random import randint


# def insertionSort(list):
#   for i in range(len(list)):
#     minIdx = i
#     for j in range(i, len(list)):
#       if list[j] < list[minIdx]:
#         minIdx = j

#     min = list[minIdx]
#     for k in range(minIdx, i, -1):
#       list[k] = list[k - 1]

#     list[i] = min

#   return list


def insertionSort(list):
  for i in range(1, len(list)):
    key = list[i]

    j = i - 1

    while j >= 0 and list[j] > key:
      list[j + 1] = list[j]
      j -= 1
    list[j + 1] = key

  return list


list = [randint(0, 10) for i in range(5)]
print(list)

print(insertionSort(list))
