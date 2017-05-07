count=input("Enter String\t")
i=0;
j=0;
for v in count:
    if v.isdigit():
        i=i+1;
    else:
        j=j+1;

print("Digit :%d and Alphabet :%d" %(i,j))
