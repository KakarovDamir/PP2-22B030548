import random
number = 7
cnt = 0
f = 1
m = 21

def r(f,m):
    global n
    n = random.randrange(f,m)
    return n

print("Hello! What is your name?")
name = str(input())
print('Well, ',name,',', ' I am thinking of a number between 1 and 20.', sep = "")
print('Take a guess.')

while(True):
    cnt += 1
    r(f,m)
    print(n)
    if n < number:
        print("Your guess is too low.")
        print("Take a guess.")
        f = n + 1
        m = 21
    elif n > number:
        print("Your guess is too high.")
        print("Take a guess.")
        
        f = 1
        m = n - 1
    else:
        print("Good job, ",name,'!', ' You guessed my number in ',cnt,' guesses!',sep = "")
        break