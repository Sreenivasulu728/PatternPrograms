n=5
sp=n-1
st=1
for x in range(n):
    num=st
    for y in range(sp):
        print(' ',end=' ')
    for z in range(st):
        print(num,end=' ')
        num-=1
    print()
    sp-=1
    st+=1