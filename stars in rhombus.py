n=int(input('enter n value: '))
sp=n//2
st=1
for s in range(n):
    for r in range(sp):
        print(' ',end=' ')
    for e in range(st):
        print('*',end=' ')
    print()
    if s<n//2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1