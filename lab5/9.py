import re 

txt = input()

x = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

print (x)