n=5
for x in range(n):
    print(' '*(n-1-x)+chr(65+x),end='')
    if x>=1:
        print(' '*(2*x-1)+chr(65+x),end='')
    print()
for x in range(n-1):
    print(' '*(x+1)+chr(68-x),end='')
    if x!=n-2:
        print(' '*((n-1)+1-2*x)+chr(68-x))
    