arr=list(map(int,(input().split())))
st=min(arr)
end=max(arr)
for i in range(st,end):
    if i+1 in arr:
        continue
    else:
        print(i+1,end=" ")

   