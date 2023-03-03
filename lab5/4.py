import re 

txt = str(input())

x = re.findall("[A-Z][a-z]+",txt)

print(x)