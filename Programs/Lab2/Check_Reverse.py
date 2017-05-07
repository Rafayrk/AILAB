
def val(name,le,va):

    if le != -1:
      va += name[le]+val(name, le-1, va)
    else:
       va = ""

    return va;




inp = input("Enter String\t")
le = len(inp)
print(val(inp, le-1, ""))