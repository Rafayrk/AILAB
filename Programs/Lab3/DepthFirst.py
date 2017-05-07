list = [[0,0,0,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,0,1,0,1]]
j=0;
for i in range(0,5):
  if(list[i][i]==1):


        print("There is a loop On index"+"["+str(i+1)+"]""["+str(i+1)+"]")

  else:
     j=j+1;


if(j==5):
    print("There is No Loop")