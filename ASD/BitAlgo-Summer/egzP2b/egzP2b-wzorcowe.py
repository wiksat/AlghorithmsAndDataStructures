from egzP2btesty import runtests
from math import log10
class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.x=0
def add2Node(root,string):
    if string =="":
        root.x+=1
        return
    root.x+=1
    if string[-1]=="1":
        if not root.left:
            root.left=Node()
        add2Node(root.left,string[:-1])
    else:
        if not root.right:
            root.right=Node()
        add2Node(root.right,string[:-1])
    return
def addprefix(root,string):
    if string=="":
        return root.x
    if string[-1]=="1":
        return addprefix(root.left,string[:-1])
    else:
        return addprefix(root.right,string[:-1])

def kryptograf(D, Q):
    # tutaj proszę wpisać własną implementację
    root=Node()
    output = 0
    for i in D:
        add2Node(root,i)
    for i in Q:
        output+=log10(addprefix(root,i))

    return output

runtests(kryptograf, all_tests=3)