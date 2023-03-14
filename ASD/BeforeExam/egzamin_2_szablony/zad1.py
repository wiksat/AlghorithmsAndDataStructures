from zad1testy import runtests


def binary_search(T, x):
    l = 0
    r = len(T) - 1
    while l <= r:
        mid = (l + r) // 2
        if T[mid] == x:
            return mid
        elif T[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1

# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     if (high >= low):
#
#         mid = low + (high - low) // 2
#         if x == arr[mid]:
#             return (mid)
#         elif (x > arr[mid]):
#             return binarySearch(arr, (mid + 1), high, x)
#         else:
#             return binarySearch(arr, low, (mid - 1), x)
#
#     return -1


def dfs(graph, visited, u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, visited, v)


def intuse(I, x, y):
    result=[]
    tab=[]
    for i in range(len(I)):
        tab.append(I[i][0])
        tab.append(I[i][1])
    tab.sort()
    wierzch_uniq=[tab[0]]
    ind=0
    for i in range(1,len(tab)):
        if wierzch_uniq[ind]!=tab[i]:
            wierzch_uniq.append(tab[i])
            ind+=1
    if binary_search(wierzch_uniq,x)==-1 or binary_search(wierzch_uniq,y)==-1:
        return []
    graf_x=[[] for _ in range(len(wierzch_uniq))]
    graf_y=[[] for _ in range(len(wierzch_uniq))]
    for i in range(len(I)):
        iks=binary_search(wierzch_uniq,I[i][0])
        igrek=binary_search(wierzch_uniq,I[i][1])
        graf_x[iks].append(igrek)
        graf_y[igrek].append(iks)
    x_visited=[False for _ in range(len(wierzch_uniq))]
    dfs(graf_x, x_visited, binary_search(wierzch_uniq,x))
    y_visited = [False for _ in range(len(wierzch_uniq))]
    dfs(graf_y,y_visited,binary_search(wierzch_uniq,y))
    for i in range(len(I)):
        iks = binary_search(wierzch_uniq, I[i][0])
        igrek = binary_search(wierzch_uniq, I[i][1])
        if x_visited[iks] and y_visited[igrek]:
            result.append(i)

    return result


runtests(intuse)