n=4
sp=0
st=7
for s in range(n):
    for r in range(sp):
        print(' ',end=' ')
    for e in range(st):
        print('*',end=' ')
    print()
    sp+=1
    st-=2