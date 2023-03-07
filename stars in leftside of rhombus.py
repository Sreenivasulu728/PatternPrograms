n=5
sp=n//2
st=1
for s in range(n):
    for r in range(sp):
        print(' ',end=' ')
    for e in range(st):
        print('*',end=' ')
    print()
    if s<2:
        sp-=1
        st+=1
    else:
        sp+=1
        st-=1