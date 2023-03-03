import re 

txt = str(input())

x = re.findall("a.*b$",txt)

print(x)