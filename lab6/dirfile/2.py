import os
print('Exist:', os.access(r'C:\Users\Дамир\Documents\pp2\lab6\dirfile', os.F_OK))
print('Readable:', os.access(r'C:\Users\Дамир\Documents\pp2\lab6\dirfile', os.R_OK))
print('Writable:', os.access(r'C:\Users\Дамир\Documents\pp2\lab6\dirfile', os.W_OK))
print('Executable:', os.access(r'C:\Users\Дамир\Documents\pp2\lab6\dirfile', os.X_OK))
