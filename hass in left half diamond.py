n=int(input('enter n value:'))
for s in range(n):
    print('  '*(n-s-1)+'# '*(s+1))
for s in range(n-1):
    print('  '*(s+1)+'# '*(n-s-1))