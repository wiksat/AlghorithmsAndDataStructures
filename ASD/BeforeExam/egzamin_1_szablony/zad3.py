from zad3testy import runtests


def kintersect( A, k ):
  """Miejsce na Twoją implementację"""
  n=len(A)
  res=[]
  interval = [(i, A[i][0], A[i][1]) for i in range(len(A))]
  interval.sort(key=lambda x: x[2], reverse=True)
  print(interval)
  max_length = 0


runtests( kintersect )