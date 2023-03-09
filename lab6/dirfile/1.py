import os
path = r"C:\Users\Дамир\Documents\pp2\lab6"

print ("Only directories:")
a = []
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path,name)):
        a.append(name)
print(a)

print("\nOnly files:")
n = []
for name in os.listdir(path):
    if not os.path.isdir(os.path.join(path,name)):
        n.append(name)
print(n)

print("\nAll directories and files:")
m=[]
for name in os.listdir(path):
    m.append(name)
print(m)
