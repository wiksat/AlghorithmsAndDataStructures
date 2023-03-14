import math

tab=[1,1,1,1,1,1,1,1]
n=len(tab)
wykladnik=math.floor(math.log2(n))
dl_drzewa=(2**wykladnik)*2
przesuniecie=(2**wykladnik)
drzewoM=[0 for _ in range(dl_drzewa)]
drzewoL=[0 for _ in range(dl_drzewa)]
drzewoR=[0 for _ in range(dl_drzewa)]
for ind,el in enumerate(tab):
    indeks=ind+przesuniecie
    if el==0:
        d=1
    else:
        d=0
    drzewoM[indeks]=d
    # if indeks%2==0:
    #     drzewoL[indeks//2]=drzewoM[indeks]
    # else:
    #     drzewoR[indeks // 2] = drzewoM[indeks]
    #     drzewoM[indeks // 2]=drzewoL[indeks//2]+drzewoR[indeks//2]
def aktualizacja(indeks):
    global n
    lewy=2*indeks

    while lewy<n:
        lewy=2*lewy+1
    lewy//=2

    if drzewoR[lewy]!=0:
        while drzewoR[lewy]>0 and drzewoL[lewy]==drzewoR[lewy] and lewy>indeks:
            lewy//=2
        if lewy==indeks:
            lewy=lewy*2

        drzewoL[indeks]=drzewoR[lewy]+drzewoL[lewy]
    else:
        drzewoL[indeks]=0
        # pass

    prawy=2*indeks+1
    while prawy<n:
        prawy=2*prawy
    prawy//=2
    # print(indeks, lewycp,prawy)
    if drzewoL[prawy] != 0:
        while drzewoL[prawy]>0 and drzewoR[prawy]==drzewoL[prawy]and prawy>indeks:
            prawy//=2
        if prawy == indeks:
            prawy = prawy * 2+1
        drzewoR[indeks] = drzewoL[prawy] + drzewoR[prawy]
    else:
        drzewoR[indeks]=0

    if drzewoL[indeks]==drzewoM[indeks*2] and drzewoR[indeks]==drzewoM[indeks*2+1]:
        drzewoM[indeks]=drzewoM[indeks*2]+drzewoM[indeks*2+1]
    else:
        drzewoM[indeks]=max(drzewoM[indeks*2],drzewoM[indeks*2+1])
def update(ind,el):
    global przesuniecie
    indeks=ind+przesuniecie
    if el==0:
        d=1
    else:
        d=0
    drzewoM[indeks]=d
    if indeks%2==0:
        drzewoL[indeks//2]=drzewoM[indeks]
    else:
        drzewoR[indeks // 2] = drzewoM[indeks]
    drzewoM[indeks // 2]=drzewoL[indeks//2]+drzewoR[indeks//2]
    indeks//=4

    while indeks!=0:
        aktualizacja(indeks)
        indeks//=2
update(0,0)
update(1,0)
update(2,0)
update(3,0)
update(4,0)
update(5,0)
update(6,0)
update(7,0)
print(drzewoM)
print(drzewoL)
print(drzewoR)
print("odpowiedz ",drzewoM[1])