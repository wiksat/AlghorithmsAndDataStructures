from zad1testy import runtests
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i][0] <= M[j][0]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def chaos_index( T ):
    # tu prosze wpisac wlasna implementacje
    n=len(T)
    for i in range(n):
        T[i]=(T[i],i)
    maxi=0
    mergeSort(T)

    print(T)
    for i in range(n):
        maxi=max(maxi,abs(T[i][1]-i))

    return maxi


runtests( chaos_index )
