def polin(mystr):
    list1 = list(mystr)
    list1.reverse()
    str2 = ""
    for x in list1:
        str2 += x
    if str2 == mystr:
        return True
    else:
        return False
mystr = str(input())
print(polin(mystr))