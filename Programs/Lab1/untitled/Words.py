word=input("Enter Word\t")
count={}
for co in word:
    if co not in count.keys():
     count[co]=1;
    else:
        count[co]=count[co]+1;

for cd in word:
    print("%s is %d times\n" %(cd,count[cd]));