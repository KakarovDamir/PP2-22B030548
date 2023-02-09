def myreverse_function(mystring):
    list1 = mystring.split(" ")
    list1.reverse()
    for x in list1:
        print(x, end = " ")

mystring = str(input())
myreverse_function(mystring)