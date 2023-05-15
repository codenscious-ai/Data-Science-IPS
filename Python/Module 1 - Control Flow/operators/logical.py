
x, y = 3, 5
print(x < y or x > y)   # True or False => True
print(x < y and x > y)  # True and False => False
print(x < y and x != y) # True or True => True
print((x < y) ^ (x != y))   # True xor True => False
print(not(x < y or x > y))   # True or False => not(True) => False
 
