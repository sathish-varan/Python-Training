"""n=int(input())
arr=list(map(int,input().split()))
lead=arr[0]

for i in range(n):
    if arr[i]>lead:
        lead=arr[i]
    print(lead,end=" ")
    count=i+1
"""
size=int(input())
n=list(map(int,input().split()))
i=0
while i <len(n):
    j=i
    maxi=n[j]
    while j<len(n):
        if n[j]>maxi:
            maxi=n[j]
            i=j
        j+=1
    print(maxi,end=" ")
    i+=1
            
   
        

        
