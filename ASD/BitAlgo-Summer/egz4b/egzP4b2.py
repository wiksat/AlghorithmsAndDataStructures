from egzP4btesty import runtests

def node_prev(root):
    if root.left:
        current=root.left
        while current.right:
            current=current.right
        return current

    p_root=root.parent
    while p_root:
        if root != p_root.left:
            break
        root=p_root
        p_root=p_root.parent
    return p_root
def node_next(root):
    if root.right:
        current=root.right
        while current.left:
            current=current.left
        return current

    p_root=root.parent
    while p_root:
        if root != p_root.right:
            break
        root=p_root
        p_root=p_root.parent
    return p_root

class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None

def sol(root, T):
    n = len(T)
    suma = 0
    for i in range(n):
        a=node_prev(T[i])
        b=node_next(T[i])
        if a.key+b.key==2*T[i].key:
            suma+=T[i].key
    return suma


runtests(sol, all_tests=True)