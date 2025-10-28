#Control flux in python
#This part of python module dscribes "if" statements

lights_status = True

if lights_status:
    print("The light is on")

print(f"The light status is {lights_status}")

'''
Comparing operators:
>
<
>=
<=
!=
'''

#less than <
a = 4
b = 6
result = a > b
print(f"a > b is {result}")

#greater than >
result = a < b
print(f"a < b is {result}")

#Greater or equal >=
a = 6
b = 6
result = a >= b 
print(f"a >= b is {result}")

#less or equal <=
a = 5
b = 6
result = a <= b 
print(f"a <= b is {result}")

#is equal to ==
a = 5
b = 6
result = a == b
print(f"a == b is {result}")

#is different than
a = 5
b = 6
result = a != b
print(f"a != b is {result}")

#conditional
a = 50
if a > 0:
    print("A is a positive number")

#Logic operator AND &&
age = 18
theory_test = 80
practical_test = True
medical_ruling = True

if age >= 18 and theory_test >= 80 and practical_test == True and medical_ruling == True:
    print("Driver's license granted")

#Logic operator OR
videogame = 'Until dawn'
reading = False
movie = False

if videogame == 'Outlast' or reading == True or movie == True:
    print("I'm happy with my hobby")

#Operator NOT
door_open = False
day = False

if not door_open: 
    print("The door is closed")

if not day:
    print("It is night time")

#if else sentence
number = int(input("Insert number "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")