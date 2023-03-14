class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
def add(first,el):
    if first is None: return el
    p=first
    q=None
    if el.val<p.val:
        first=el
        el.next=p
    while p is not None and el.val>p.val:
        q=p
        p=p.next
    el.next=p
    q.next=el
    return first

def remove(first,el):
    p=first
    if p is el:
        return p.next
    if first is None:
        return None
    while p.next is not None:
        if p.next is el:
            p.next=p.next.next
            return first
        p=p.next
    return first
# w miare optymalny
def sort(first):
    sorted=None
    p=first
    while p is not None:
        q=p
        p=p.next
        q.next=None
        sorted=add(sorted,q)
    return sorted


#                       insert      select      bubble
# o(srednie)             n^2      n^2         n^2
# teta(pesymistyczne)    n^2      n^2         n^2
# omega(optymistyczne)   n        n^2         n

def min_max(T):
    min=T[0]
    max=T[1]
    n=len(T)
    for i in range(0,n,2):
        if T[i]>T[i+1]:
            m=T[i]#wieksza
            n=T[i+1]#mniejsza
        else:
            m=T[i+1]
            n=T[i]
        if m>max:
            max=m
        if n<min:
            min=n
    return min,max