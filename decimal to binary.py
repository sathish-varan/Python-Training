n= int(input())
binary,decimal=0,1
while n>0:
    rem=n%2
    binary=binary+(rem*decimal)
    decimal*=10
    n=n//2
print(binary)
