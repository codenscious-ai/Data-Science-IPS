# we will impliment a simple cqalculator

x = int(input("enter the vaqlue of x : "))
y = int(input("enter the vaqlue of y : "))
op = input("Eerer \n+ to add \n- to subtract \n* to multiply and \n/ to devide \n enter the operator...  : ")

valid_op = True

if op == '+':
    z = x + y

elif op == '-':
    z = x - y
    

elif op == '*':
    z = x * y
    
elif op == '/':
    z = x / y    

else:
    print("Invalid input")
    valid_op = False

if valid_op == True:
    print("The result is", z)

