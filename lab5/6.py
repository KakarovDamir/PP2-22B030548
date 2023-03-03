import re 

txt = str(input())

x = re.sub("\s",",",txt) 
y = re.sub("\.",":",x)

print(y)