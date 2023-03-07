n=int(input('enter n value: '))
st=1
for s in range(n):
    for r in range(st):
        print('*',end=' ')
    print()
    if s<n//2:
        st+=1
    else:
        st-=1