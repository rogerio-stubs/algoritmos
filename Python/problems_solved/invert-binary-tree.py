class BinaryTree:
  value = 0
  left = None
  right = None


def show_tree(tree):
  pass

def solution(tree):
  if tree.left is None and tree.right is None:
    return tree

  tree.left, tree.right = tree.right, tree.left
 
  if tree.left is not None:
    # print('left', tree.left.value)
    tree.left = solution(tree.left)
    
  if tree.right is not None:
    # print('right', tree.right.value)
    tree.right = solution(tree.right)

  return tree
  




if __name__ == '__main__':
  tree = BinaryTree()

  tree.value = 10
  tree.left = BinaryTree()
  tree.left.value = 2

  tree.right = BinaryTree()
  tree.right.value = 3
  tree.right.right = BinaryTree()
  tree.right.right.value = 5

  invert = solution(tree)

  print(tree.right.value)
  print(invert.right.value)

