from BST_Correct import T as bst

tree = bst(3)
tree.tree_insert(3)
tree.tree_insert(3)
tree.tree_insert(1)
tree.tree_insert(2)
tree.tree_insert(4)
tree.tree_insert(8)
tree.tree_insert(6)
tree.tree_insert(13)
tree.tree_insert(10)
tree.tree_insert(12)
tree.tree_insert(11)
tree.tree_insert(9)
tree.tree_insert(17)
tree.tree_insert(20)
tree.tree_insert(15)
tree.tree_insert(16)
tree.tree_insert(14)

while tree.root != None:
  tree.tree_delete(tree.root)
print('done')
