from egzP6btesty import runtests 

def jump ( M ):
    #tutaj proszę wpisać własną implementację
    n=len(M)
    x=0
    y=0
    dict = {}
    dict[str(x) + ":" + str(y)] = True
    for i in range(n):
        if M[i]=="LU":
            x-=2
            y+=1
        elif M[i]=="UL":
            x-=1
            y+=2
        elif M[i]=="UR":
            x+=1
            y+=2
        elif M[i]=="RU":
            x+=2
            y+=1
        elif M[i]=="RD":
            x+=2
            y-=1
        elif M[i]=="DR":
            x+=1
            y-=2
        elif M[i]=="DL":
            x-=1
            y-=2
        elif M[i]=="LD":
            x-=2
            y-=1
        if dict.get(str(x)+":"+str(y)) is not None:
            if dict.get(str(x)+":"+str(y))==True:
                dict[str(x)+":"+str(y)]=False
            else:
                dict[str(x) + ":" + str(y)] = True
        else:
            dict[str(x)+":"+str(y)]=True
    licznik=0
    for k, v in dict.items():
        if v:
            licznik+=1
    return licznik
    
runtests(jump, all_tests = True)