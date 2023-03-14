from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def wybory(T):
    #tutaj proszę wpisać własną implementację
    n=len(T)
    suma=0
    for i in range(n):
        profity = []
        wagi = []
        temp=T[i]
        tempCopy=temp
        while temp is not None:
            wagi.append(temp.koszt)
            profity.append(temp.wyborcy)
            temp=temp.next
        B=tempCopy.fundusze
        n2=len(wagi)
        F=[[0 for _ in range(B +1)]for _ in range(n2)]
        for l in range(wagi[0],B+1):
            F[0][l]=profity[0]
        for l in range(B+1):
            for i in range(1,n2):
                F[i][l]=F[i-1][l]
                if l-wagi[i]>=0:
                    F[i][l]=max(F[i][l],F[i-1][l-wagi[i]]+profity[i])
        # print(wagi,profity,F[n2-1][B])
        suma+=F[n2-1][B]

    return suma

runtests(wybory, all_tests = True)