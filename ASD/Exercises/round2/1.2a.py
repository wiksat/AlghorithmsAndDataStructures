"""
F(i,j)-dl najdluzszego wspolnego podciagu ciagów A[0,,,i], B[...j]
f(0,j)=
f(i,0)=
f(i,j)={
       f(i-1,j-1)+1 ,jeśli A[i]=B[j]
       max(f(i,j-1),f(i-1,j)  ,jeśli A[i]!=B[j]


"""