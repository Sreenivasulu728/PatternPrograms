n=4
sp=0
st=4
for x in range(n):
    for y in range(sp):
        print(' ',end=' ')
    for z in range(st):
        print('*',end=' ')
    print()
    sp+=1
    st-=1

