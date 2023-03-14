#mergesort na seriach naturalnych
def Merge(L1,L2):
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    if L1.val>L2.val:
        L1,L2=L2,L1
    head=L1
    L1=L1.next
    curr=head
    curr.next=None
    while L1 is not None and L2 is not None:
        if L1.val>L2.val:
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

    while len(heads)>1:
        heads2=[]
        while len(heads)>1:
            merged=Merge(heads[0],heads[1])
            heads2.append(merged)
            heads=heads[2:]
            heads2.extend(heads)
            heads=heads2
    return heads[0]