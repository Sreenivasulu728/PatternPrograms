n=int(input('enter n value: '))
for s in range(n):
    print('  '*(n-s-1),end='')
    for r in range(s+1):
        print('* ',end='')
    print()