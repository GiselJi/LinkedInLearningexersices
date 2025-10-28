print('Welcome to visual studio code')

print('Hello world!')

#new variable with numerical value, value is assigned from right to left as follows
num = 2
print(num)

#Integer variables: Only positive and integer numbers
age = 24
months = 5
door_quantity = 4

num_1 = 2
num_2 = 5

sum_result = num_1 + num_2

print(sum_result)

#Float variables: Numbers with decimal values
pi = 3.14
radius = 2

circle_area = pi * (pow(radius,2))
print(circle_area)

#Boolean or bool: 0 or 1 value, true or false, similar to interruptor
sunny = True
rainny = False

print(sunny)
print(rainny)

#Strings: usually text is defined in here python allows using both "" and ''
greeting = "Hello world!"
letter = 'a'

print(greeting)
print(letter)

#Change different data types into ints
example_num = "38"
example_num = int(example_num)
print(example_num)
print(type(example_num))

#String size
print(len(greeting))

#Change to CAPS
print(greeting.upper())

#Change to lower
print(greeting.lower())

#Replace text in string
phrase = "Oye como va mi ritmo, bueno pa gozar"
newphrase = "mulata"
print(phrase.replace("bueno pa gozar", "mulata"))

#Separate string according to specific character
print(phrase.split(" "))

#Find position in string
print(phrase.find("como"))

#How to find out data type from string
example_num = "40"
print(example_num.isdigit())
print(example_num.isnumeric())
print(example_num.isdecimal())

#Print ints with strings
age = 30
name = "Gisel"

print("My name is", name, "and I'm", age, "years old" )
print("My name is {} and I'm {} years old".format(name,age))
print(f"My name is {name} and I'm {age} years old")

#Insert sum values from terminal
num_1 = input("Insert first number")
num_2 = input("Insert second number")

sum_result = int(num_1) + int(num_2)

print(f"Sum result of numbers is: {sum_result}")

#This is a one line comment

'''
This
Is a multiple
Line comment
'''

print("This code will execute.")