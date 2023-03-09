my_list = ['apple', 'banana', 'cherry']

with open('my_file.txt', 'w') as f:
    for item in my_list:
        f.write("%s\n" % item)

g = open('my_file.txt', 'r')
print(g.read())