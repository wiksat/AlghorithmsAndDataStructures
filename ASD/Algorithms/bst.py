def successorPredecator(root,val):
    global suc,pre
    if root.key==val:
        if root.left is not None:
            tmp = root.left
            while (tmp.right):
                tmp = tmp.right
            pre = tmp

        if root.right is not None:
            tmp = root.right
            while (tmp.left):
                tmp = tmp.left
            suc = tmp
    else:
        if val<root.key:
            suc = root
            successorPredecator(root.left, val)
        else:
            pre=root
            successorPredecator(root.right, val)


# with parent
def minValue(node):
    current = node

    # loop down to find the leftmost leaf
    while (current is not None):
        if current.left is None:
            break
        current = current.left

    return current
def inOrderSuccessor(n):
    # Step 1 of the above algorithm
    if n.right is not None:
        return minValue(n.right)

    # Step 2 of the above algorithm
    p = n.parent
    while (p is not None):
        if n != p.right:
            break
        n = p
        p = p.parent
    return p

class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root