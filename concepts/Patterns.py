# *
# **
# ***
# ****
n=5
for i in range(n):
    for j in range(i):
        print('*',end='')
    print()
# efficient
for i in range(n):
    print('*'*i)

#      1
#     121
#    12321
#   1234321
#  123454321
n=6
for i in range(1,n):
    print(' '*(n-i),end='')
    for j in range(1,i):
        print(j,end='')
    for j in range(i,0,-1):
        print(j,end='')
    print()


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

k=1
for i in range(n):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()

#     *
#    ***
#   *****
#  *******

n=5
for i in range(1,n):
    print(' '*(n-i),'*'*(i*2-1))

#      * 
#     * * 
#    * * * 
#   * * * * 
n=5
for i in range(1,n):
    print(' '*(n-i),'* '*i)


#  * * * * * 
#  * *   * * 
#  *   *   * 
#  * *   * * 
#  * * * * *

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j== n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()