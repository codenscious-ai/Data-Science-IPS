#Find if num is prime or not

num = int(input("Enter the value of n : "))


div, is_prime = 2, True
while div < num:
    if num % div == 0:
        print("Not Prime")
        is_prime = False
        break
    else:
        div += 1

if is_prime == True:
    print("Prime")
