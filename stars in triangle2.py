n=4
sp=3
st=1
for s in range(n):
    for r in range(sp):
        print(' ',end=' ')
    for e in range(st):
        print('*',end=' ')
    print()
    sp-=1
    st+=1