row,col=map(int,input().split())
mat=[]
flag=0
for i in range(row):
    mat.append(list(map(int,input().split())))
for i in range(row):
    for j in range(col):
        if i==j and mat[i][j]==0:
            flag=1
            break
        elif i!=j and mat[i][j]!=0:
            flag=1
            break
if flag==1:
    print("Not an diagonal matrix")
else:
    print("Diagonal matrix")
            
            
