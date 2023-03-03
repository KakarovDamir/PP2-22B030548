import re 

txt = input()

print(re.findall('[A-Z][a-z]+', txt))
