import queue

print("\t\t\t\t\t\t\t\t\t\t*******Breadth First Algorithm******")

l=[[0,1,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

frontier = queue.Queue()

frontier.put(0)

explored=[]

#target=8;
target=int(input("\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Target:"))

length=len(l)

k=0;

n=True

find=False

while (n) :

  if(target>=length):
     break
  k=frontier.get()

  explored.append(k)

  if k == target:

     find=True

     break

  for j in range(0,9):

      if l[k][j]==1:

          if j not in frontier.queue and j not in explored:

            frontier.put(j)

if(find==True):

    print("\t\t\t\t\t\t\t\t\t\t\t",explored)

else:

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t ","Not Found")




