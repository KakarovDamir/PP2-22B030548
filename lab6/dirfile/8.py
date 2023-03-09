import os

path = r"C:\Users\Дамир\Documents\pp2\lab6\dirfile\D.txt"

if os.path.exists(path):

    if os.access(path, os.W_OK):
        os.remove(path)
        print(f"The file at {path} has been deleted.")
    else:
        print(f"You do not have permission to delete the file at {path}.")
else:
    print(f"The file at {path} does not exist.")
