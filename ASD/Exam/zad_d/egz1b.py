from egz1btesty import runtests
# Złożonośc obliczeniowa O(3n) = O(n), Złożonośc pamięciowa O(n)
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
    poziomy = []
    n = 0
    def Make_depths(T, dl):
        nonlocal poziomy,n
        if (T is None):
            return
        if dl + 1 > n:
            n+=1
            poziomy.append(0)
        poziomy[dl] += 1
        T.x = [dl,False]
        Make_depths(T.left, dl + 1)
        Make_depths(T.right, dl + 1)
    Make_depths(T,0)
    maxi = max(poziomy)
    index = 0
    for a in range(n-1,-1,-1):
        if(poziomy[a] == maxi):
            index = a
            break
    def Leaves_assingment(T):
        nonlocal index
        if (T is None):
            return
        if(T.x[0] == index):
            T.x[1] = True
        Leaves_assingment(T.left)
        Leaves_assingment(T.right)
        if(T.left is not None and T.left.x[1] == True):
            T.x[1] = True
        if(T.right is not None and T.right.x[1] == True):
            T.x[1] = True
    Leaves_assingment(T)
    counter = 0
    def Result(T):
        nonlocal counter
        if (T is None):
            return
        if(T.x[1] is False):
            counter += 1
            return
        Result(T.left)
        Result(T.right)
    Result(T)
    return counter

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )