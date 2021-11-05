def dfs(root):
  stack = []
  curr = root

  while curr or len(stack):
    while curr:
      stack.append(curr)
      curr = curr.left

    curr = stack.pop()
    print(curr.key, end=' ')
    curr = curr.right
