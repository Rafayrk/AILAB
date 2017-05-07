list = [[0,0,0,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,0,1,1,0]]
j=int(input("Enter To Find\t"))
j=j-1;
k=l=0;
for i in range(0,5):
    k=k+list[j][i]
    l = l + list[i][j]

print("OutDegree:"+str(k)+" InDegree:"+str(l))

