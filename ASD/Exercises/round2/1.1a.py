#subset sum
#suma podzbioru
"""
czy da się lub czy się nie da osiągnąć daną liczbę z danych danych
A=[1,7,2,8,3,5]
T=6

n=len(A)
f(i,s)={True-istnieje podciąg o sumie S {a0,...,ai},
        False-w przeciwnym razie}

f(i,s)={f(i-1,s) lub f(i-1,s-A[i])   ,s>=A[i]
        f(i-1,s)                    ,s<A[i]}
f(0,s)={True   ,  s=A[0]
        False, s!=A[0]}
"""
# A=[1,7,2,8,3,5]
A=[1,3,6,7]
# T=6
T=8
def subsetSum(A,T):
    n=len(A)
    F=[[False for _ in range(T+1)]for _ in range(n)]
    F[0][A[0]]=True
    F[0][0]=True
    for i in range(n):
        F[i][0]=True
    for i in range(1,n):
        for t in range(T+1):
            F[i][t]=F[i-1][t]
            if t>=A[i]:
                F[i][t]=F[i-1][t-A[i]] or F[i-1][t]
    for x in F:
        print(x)
    return F[n-1][T]
print(subsetSum(A,T))

# def subsetSum(A, k):
#     n = len(A)
#
#     # `T[i][j]` stores true if subset with sum `j` can be attained
#     # using items up to first `i` items
#     T = [[False for x in range(k + 1)] for y in range(n + 1)]
#
#     # if the sum is zero
#     for i in range(n + 1):
#         T[i][0] = True
#
#     # do for i'th item
#     for i in range(1, n + 1):
#         # consider all sum from 1 to sum
#         for j in range(1, k + 1):
#             # don't include the i'th element if `j-A[i-1]` is negative
#             if A[i - 1] > j:
#                 T[i][j] = T[i - 1][j]
#             else:
#                 # find the subset with sum `j` by excluding or including the i'th item
#                 T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]
#
#     # return maximum value
#     for x in T:
#         print(x)
#     return T[n][k]
# print(subsetSum(A,T))