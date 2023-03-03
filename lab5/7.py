import re

def f(snake):
    camel=re.sub('_',' ',snake)
    camel=camel.title()
    camel=re.sub(' ','',camel)
    print(camel)

snake = input()

f(snake)
