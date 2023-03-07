n=7
st=1
sp=n//2
for x in range(n):
    num=1
    for y in range(sp):
        print(' ',end=' ')
    for z in range(st):
        print(num,end=' ')
        num=num+1 if z< st//2 else num-1
    print()
    if x<n//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2