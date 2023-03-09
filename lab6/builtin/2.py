mystr="KAKAROVdamir"

l=0
up=0

for i in mystr:
      if i.islower():
            l+=1
      elif i.isupper():
            up+=1

print("The number of lowercase characters is:",l)
print("The number of uppercase characters is:",up)