def add(i, j):
    return i + j


def sub(i, j):
    return i - j


def div(i, j):
    return i / j


def mul(i, j):
    return i * j


val = int(input("Enter Num1\t"))

val2 = int(input("Enter Num2\t"))

val3 = input("Enter Operation\t")

if val3 == "+":
    print("%s + %s = %d" % (val, val2, add(val, val2)))
elif val3 == "-":
   print("%s + %s = %d"%(val,val2,sub(val,val2)))
elif val3 == "*":
    print("%s + %s = %d" % (val, val2, mul(val, val2)))
elif "/" == val3:
    print("%s + %s = %d" % (val, val2, div(val, val2)))
else:
    print("Unknown Operator")