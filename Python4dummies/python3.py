#Python lists
my_fruits = ["apple", "grape", "pineapple", "apple", "Kiwii", "strawberry"]
print(my_fruits)

my_numbers = [1, 5, 2, 6, 7, 40]
print(my_numbers)

my_info = ["Gisel", 30, True]
print(my_info)

#For printing each array place
for fruit in my_fruits:
    print(fruit)

#while cicle printing numbers
number = 0
while number <= 100:
    print(number)
    number += 1

number = 1
while number <= 50:
    print(number)
    number += number


#break in python
for second in range(20): 
    if second == 10:
        print("Stop car")
        break
    print(second)

#continue in python
tasks = ["sweep", "do the dishes", "do the laundry", "cook", "clean the furniture"]

for task in tasks:
    if task == "do the laundry":
        print(f"Will do the following task: {task}")
        continue
    print("Task completed", task)

#managing lists in python
my_fruits = ["apple", "grape","strawberry", "dragon fruit"]
my_fruits[2] = "mango"
print(my_fruits)

#Add a new element to my list
my_fruits.append("orange")
print(my_fruits)

#remove specific element from my list
my_fruits.remove("grape")
print(my_fruits)

#remove last element from my list
my_fruits.pop()
print(my_fruits)

#sort my list by alphabetic order
my_fruits.sort()
print(my_fruits)