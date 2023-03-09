g = open ('haha.txt','r')
content = g.read()

y = open ("A.txt", 'w')
y.write(content)
y = open ("A.txt", 'r')

print(y.read())