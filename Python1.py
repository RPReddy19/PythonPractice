
# print("Hello, World!")

# variables

name = "Rana Prathap Reddy"    # String
age = 30                       # Integer
height = 5.10                  # Float
is_employee = True             # Boolean

print(type(name))
print(type(age))
print(type(height))
print(type(is_employee))

print(name)
print(age)
print(height)
print(is_employee)


# basic arithmetic operations 

a = 10 
b = 20

sum_result = a + b
diff_result = a - b
product_result = a * b
divide_result = a / b
modulus_result = a % b 
exponent_result = a ** b

print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", product_result)
print("Division:", divide_result)
print("Exponent", exponent_result)



# comparison operators

print(a == b)    #False
print(a != b)    #True
print(a > b)     #False
print(a < b)     #True
print(a >= b)    #False
print(a <= b)    #True

# Logical operators

x = True
y = False
print(x and y)      #False
print(x or y)       #True
print(not x)        #False

# contral statements

number = int(input("Enter a number:"))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    
# Loops
  
for i in range(10):
    print(i)        # prints 0 to 9
    
    
# while

count = 0
while count < 10:
    print(count)
    count += 1  # Incriment count
    
    
    
    # Data Structures
    
# Lists 
# An ordered collection of items that can be changed
    
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple because count starts from 0
fruits.append("orange")
print(fruits) # 'apple', 'banana', 'cherry', 'orange'

# Tuples - cannot be changed

colors = ("red", "blue", "green")
print(colors)
print(colors[1])

# Directories - An unordered collection of key-value pairs

person = {"name": "Rana", "age": 31}
print(person)

print(person ["name"])
person["age"] = 32
print(person)


# Sets -  unoredered collecton of unique items 

unique_numbers = {1, 2, 3, 4, 5, 5}
print(unique_numbers)

unique_numbers.add(7)
print(unique_numbers)




# Functions

def greet(name):
    return f"hello.{name}!"
print(greet("Rana"))

# Paramenters and return values

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))  #120

# defualt parameters

def power(base, exp = 2):
    return base ** exp
print(power(3))
print(power(3, 3))

# lambda functions - anonymous fucntions are defined with lambda

add = lambda x, y : x + y
print(add(5,0))




    
    
    
    