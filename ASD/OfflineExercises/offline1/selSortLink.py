class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
def print_node(first):
    current=first
    while current is not None:
        print(current.val,"-->", end="")
        current=current.next
    print()
def tab2list(t):
    n = len(t)
    p = None

    for i in range(n-1,-1,-1):
        q = Node()
        q.val = t[i]
        q.next = p
        p = q
    return p

def selSort(tab,k):
    for i in range(len(tab)):
        min_idx = i
        for j in range(i + 1, i+k+1):
            if i+k<len(tab):
                if tab[min_idx] > tab[j]:
                    min_idx = j
        tab[i], tab[min_idx] = tab[min_idx], tab[i]

def selSortForLinkedList(p,k):
    e=p
    prev_minim = None
    prev_p=None
    f=0
    while p is not None:
        w=p
        minim=p
        wyn=0
        flag=0
        for n in range(1,1+k):
            if w.next is not None:
                s=w
                w=w.next
                if minim.val>w.val:
                    prev_minim=s
                    minim=w
                    wyn=n
                    flag=1

        if flag==1:
            if wyn!=1:
                # print_node(e)
                copy_min_next=minim.next
                minim.next=p.next
                p.next=copy_min_next
                # print(copy_min_next.val)
                if prev_minim is not None:
                    prev_minim.next=p
                if prev_p is not None:
                    prev_p.next=minim
                # print_node(e)
            else:
                copy_min_next = minim.next
                p.next = copy_min_next
                if prev_p is not None:
                    prev_p.next = minim
                minim.next=p
        print_node(e)
        p=minim

        if f == 0:
            e=p
        prev_p = p
        p=p.next
        f=1
    return e
tab=[1,3,4,2,5,7,6,9]
# tab=[9,3,4,2,5,7,6,1]
# selSort(tab,2)
print(tab)
lista=tab2list(tab)
print_node(lista)
print()
lista=selSortForLinkedList(lista,2)
print_node(lista)
