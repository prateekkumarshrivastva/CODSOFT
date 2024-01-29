print('''
+ add
- subtract
* multiply
/ divide
''')

num1=float(input("enter the value1:-"))
num2=float(input("enter the value2:-"))
opr=(input("enter the opr.."))
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid opr....")