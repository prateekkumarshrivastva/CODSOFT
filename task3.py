import random
import string
charLetter=string.ascii_letters
digit=string.digits
simboles=string.punctuation
total=charLetter+digit+simboles
length=int(input("enter the length of password: ",))
x=random.sample(total,length)
password="".join(x)
print("\n",password,"\n")
