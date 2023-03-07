n=7
st=1
sp=n//2
for x in range(1,n+1):
    num=1
    if x%2==0:
        num=2
    for y in range(sp):
        print(' ',end=' ')
    for z in range(st):
        print(num,end=' ')
        if x%2==0:
            num=num+2 if z<n//2 else num-2
        else:
            num=num+1 if z<n//2 else num-1

    print()
    if x<n//2+1:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
    