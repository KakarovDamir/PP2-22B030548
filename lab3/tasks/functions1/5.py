from itertools import permutations 

def p(mystring):

    list1 = mystring.split(" ")
    perm = permutations(list1)

    for i in list(perm):
        print(i)
        
mystring = str(input())
p(mystring)


