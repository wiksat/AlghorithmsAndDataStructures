def SortH(p,k):

    n = 0
    q = p
    while q is not None:
        n += 1
        q = q.next

    if k < 20 and n < 50:

        def insertionSort(head_ref):

            sorted = None

            current = head_ref

            while current is not None:

                next = current.next

                sorted = sortedInsert(sorted, current)

                current = next

            head_ref = sorted
            return head_ref


        def sortedInsert(head_ref, new_node):
            current = None

            if (head_ref == None or (head_ref).val >= new_node.val):

                new_node.next = head_ref
                head_ref = new_node

            else:

                current = head_ref
                while (current.next != None and
                       current.next.val < new_node.val):
                    current = current.next

                new_node.next = current.next
                current.next = new_node

            return head_ref

        insertionSort(p)


    # insertion_sort

    else:
        tablica = [0]*n

        start = p

        for i in range(n):
            tablica[i] = p.val
            p = p.next


        def heapify(arr, n, i):

            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i] < arr[l]:
                largest = l

            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)

            for i in range(n // 2, -1, -1):
                heapify(arr, n, i)

            for i in range(n - 1, 0, -1):

                arr[i], arr[0] = arr[0], arr[i]


                heapify(arr, i, 0)


        heapSort(tablica)


        p = start

        for i in range(n):
            p.val = tablica[i]
            p = p.next

        return start