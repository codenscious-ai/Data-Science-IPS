#Find if num is prime or not

num = int(input("Enter the value of n : "))


div = 2
while div < num:
    if num % div == 0:
        print("Not Prime")
        break
    elif div < num:
        div += 1
    if div == num: 
        print("Prime")

