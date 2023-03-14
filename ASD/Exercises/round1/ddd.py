class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None
#mergesort na seriach naturalnych
def Merge(L1,L2):
    inv=0
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    if L1.val>L2.val:
        L1,L2=L2,L1
        inv+=1
    head=L1
    L1=L1.next
    curr=head
    curr.next=None
    while L1 is not None and L2 is not None:
        if L1.val>L2.val:
            inv+=1
            L1,L2=L2,L1
        curr.next=L1
        L1=L1.next
        curr=curr.next
        curr.next=None
    if L1 is None:
        curr.next=L2
    else:
        curr.next=L1
    return head

def mergeSort(L):
    heads=[]
    while L is not None:
        head=L
        curr=L
        while curr.next is not None and curr.val<curr.next.val:
            curr=curr.next
        heads.append(head)
        L=curr.next
        curr.next=None
        print("idzie")

    heads2=[]
    inv=0
    while len(heads)>1:
        print("idzie do merga",len(heads))
        merged=Merge(heads[0],heads[1])

        # print(heads,heads2)
        heads2.append(merged)
        # print(heads,heads2)
        heads=heads[2:]
        # print(heads,heads2)
        heads2.extend(heads)
        # print(heads,heads2)
        heads=heads2[:]
        # print(heads,heads2)
        heads2=[]
    return heads[0],inv
arr = [1, 20, 6, 4, 5]
lista=Node(1)
lista2=Node(20)
lista3=Node(6)
lista4=Node(4)
lista5=Node(5)
lista.next=lista2
lista2.next=lista3
lista3.next=lista4
lista4.next=lista5
print(lista)
print(mergeSort(lista))
