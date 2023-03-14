def binarySearch(arr, low, high, x):
    if (high >= low):

        mid = low + (high - low) // 2
        if x == arr[mid]:
            return (mid)
        elif (x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)

    return -1
tab=[2,4,6,77,87,90]
print(binarySearch(tab,0,len(tab)-1,87))