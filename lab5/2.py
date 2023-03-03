import re 

txt = str(input())

x = re.findall("a.{2,3}b",txt)

print(x)