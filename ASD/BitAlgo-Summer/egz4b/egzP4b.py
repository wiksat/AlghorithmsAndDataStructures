from egzP4btesty import runtests

def findPreSuc(root, key):
  # Base Case
  if root is None:
    return

  # If key is present at root
  if root.key == key:
    # the maximum value in left subtree is predecessor
    if root.left is not None:
      tmp = root.left
      while (tmp.right):
        tmp = tmp.right
      findPreSuc.pre = tmp

    # the minimum value in right subtree is successor
    if root.right is not None:
      tmp = root.right
      while (tmp.left):
        tmp = tmp.left
      findPreSuc.suc = tmp
    return

  # If key is smaller than root's key, go to left subtree
  if root.key > key:
    findPreSuc.suc = root
    findPreSuc(root.left, key)

  else:  # go to right subtree
    findPreSuc.pre = root
    findPreSuc(root.right, key)

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None

def sol(root, T):
    n=len(T)
    suma=0
    for i in range(n):
      findPreSuc.pre = None
      findPreSuc.suc = None
      findPreSuc(root, T[i].key)
      if T[i].key==(findPreSuc.pre.key+findPreSuc.suc.key)/2:
        suma+=(findPreSuc.pre.key+findPreSuc.suc.key)/2
    return suma
    
runtests(sol, all_tests = True)