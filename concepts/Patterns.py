n=6
for i in range(1,n):
    print(' '*(n-i),end='')
    for j in range(1,i):
        print(j,end='')
    for j in range(i,0,-1):
        print(j,end='')
    print()
for i in range(1,n):
    print(' '*(n-i),'*'*(i*2-1))

k=1
for i in range(n):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()
    