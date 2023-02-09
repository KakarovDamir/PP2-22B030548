def func(list1):
    str1 = ""
    for x in list1:
        if x == '0' or x == '7':
            str1 += x
        else:
            continue
    if str1 == "007":
        print(True, str1)
    else:
        print(False, str1)
list1 = list(input().split())
func(list1)
