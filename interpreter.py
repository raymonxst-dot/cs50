num1,op,num2=input('enter:').split(' ')
num1=float(num1)
num2= float(num2)
#Python are spliting datas between (num1,op,num2) and changing their type to float
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '%':
    print(num1 % num2)