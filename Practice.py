n=5
for x in range(n):
    print(' '*(n-1-x)+chr(65+x),end='')
    if x>=1:
        print(' '*(2*x-1)+chr(65+x),end='')
    print()
for y in range(n-2):
    print(' '*(y+1)+chr(68-y)+' '*((n-1)+1-(2*y))+chr(68-y))
print(' '*(n-1)+chr(65))
    