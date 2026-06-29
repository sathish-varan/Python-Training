n= int(input())
p=1
while(n!=0):
    s=n%10
    p=p*s
    n=n//10
print(p)
