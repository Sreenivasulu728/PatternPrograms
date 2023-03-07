n=7
sp=n//2
st=1
for x in range(n):
    num=st
    for y in range(sp):
        print(' ',end=' ')
    for z in range(st):
        print(num,end=' ')
        num-=1
    print()
    if x<n//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2