n=int(input())
binary=0
decimal=1
while n>0:
    rem=n%10
    binary= binary+(rem*decimal)
    decimal*=2
    n=n//10
print(binary)
