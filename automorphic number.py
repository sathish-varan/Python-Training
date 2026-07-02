"""n=int(input())
count=0
sqr=n*n
temp=n
while temp>0:
    count+=1
    temp//=10
if n==sqr%(10**count):
    print("automorphic number")
else:
    print("no")
"""

def digitcount(n):
    if n<10:
        return 1
    return 1 + digitcount(n//10)
n=int(input())
if ((n*n)%(10**digitcount(n))==n):
    print("yes")
else:
    print("no")
