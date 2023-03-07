n=5
sp=n//2
st=1
num=5
for x in range(n):
    for y in range(sp):
        print(' ',end=' ')
    for z in range(st):
        print(num,end=' ')
        num-=1
    print()
    num=5
    if x<n//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2