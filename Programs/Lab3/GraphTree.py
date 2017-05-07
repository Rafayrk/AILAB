list = [[0,0,0,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,0,1,0,0]]
i=int(input("Enter Adjancence\t"))
i = i-1
for j in range(0,5):
  if(list[i][j]==1):
     {
        print("On["+str(j+1)+"] :"+str(list[i][j]))
      }

