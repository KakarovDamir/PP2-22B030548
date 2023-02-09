class Account:
    def __init__(self,owner,balance,deposit):
        self.owner = owner
        self.balance = balance
        self.deposit = deposit

    def dep(self,howmuch):
        self.howmuch = howmuch
        if self.howmuch > self.balance:
            print("You don't have enough funds\n")
        else:
            self.balance -= self.howmuch
            self.deposit += self.howmuch
            print(f"The operation was successful, you have {self.balance} left on your balance and on your deposit balance {self.deposit}\n")
    
    def wd(self, kansha):
        self.kansha = kansha
        if self.kansha > self.balance:
            print("You don't have enough funds\n")
        else:
            self.balance -= self.kansha
            print(f"The operation was successful, you have {self.balance} left on your balance\n")

print ("Creating a bank account:")
a = str(input("Enter your name: "))
b = int(input("Enter your balance: "))
c = int(input("Enter your deposit balance: "))
acc = Account(a,b,c)

while True:
    c = str(input("choose what you want to do : \n (deposit) (withdraw) (balance) (exit) \n"))
    if c == "deposit":
        d = int(input('write the amount: '))
        acc.dep(d)
    elif c == "withdraw":
        f = int(input('write the amount: '))
        acc.wd(f)
    elif c == "balance":
        print (f"Your balance: {acc.balance} \n")
    elif c == "exit":
        print(f"Thank you {acc.owner}, have nice day, goodbay")
        break
    else:
        print("We don't have this option, please select again\n")
        
