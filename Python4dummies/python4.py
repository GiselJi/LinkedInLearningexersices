#Tuples are a colection of inmutable and sorted elements in python written
#with parenthesis
lugagge = ("shirt", "shoes", "pants", "shoes", "dress", "socks", "shoes")

#lugagge[0] = "coat" TypeError: 'tuple' object does not support item assignment
print(lugagge[0])

#how to get number of the same element
shoe_pairs = lugagge.count("shoes")
print(shoe_pairs)

#how to know element index
first_shoes = lugagge.index("shoes")
print(first_shoes)

#print my tuple
for garment in lugagge:
    print(garment)


#Sets in python, similar to lists but with {}, unique elements not sorted
guests = {"Luis", "Ana", "Sebastian", "Sofia", "Mateo", "Ana", "Sebastian"}
print(guests)

#print(guests[0]) TypeError: 'set' object is not subscriptable
for guest in guests:
    print(f"Guest name: {guest}")

guests = {"Luis", "Ana", "Sebastian", "Sofia", "Mateo", "Valeria"}
print(guests)

#Add element to set
guests.add("Isabel")
print(guests)

#Remove element from set
guests.remove("Sebastian")
print(guests)

#Remove element from set with no error if not found
guests.discard("Valeria")
print(guests)

#Remove last element from set with no specific order
guests.pop()
print(guests)

#Dictionaries in python, created with {} separated with ,
contacts = {
    "Ana": "(123) 456-7891",
    "Luis": "(456) 789-1011",
    "Rose": "(121) 314-1516",
    "Sebastian": "(171) 819-2021",
    "Sofia": "(222) 324-2526"
}
print(contacts)

print(contacts["Luis"])

rose_info = contacts.get("Rose")
print(rose_info)

contact_keys = contacts.keys()
print(contact_keys)

contact_values = contacts.values()
print(contact_values)

#update dictionary value
contacts.update({"Sofia": "(303) 132-3334"})
print(contacts)

#update dictionary value
contacts["Ana"] = "(404) 142-4344"
print(contacts)

contacts["Mateo"] = "(505) 152-5354"
print(contacts)

#remove from dictionary
contacts.pop("Luis")
print(contacts)

#print all elements from dictionary
for keys, value in contacts.items():
    print(f"Name: {keys} Phone: {value}")

#Matrix in python, similar to an excel table, list of lists
clientes = [
            ["Cally", "Reynolds", "penatibus.et@lectusa.com",	"(901) 166-8355"], 
            ["Sydney",	"Bartlett",	"nibh@ultricesposuere.edu",	"(982) 231-7357"], 
            ["Hunter",	"Newton",	"quam.quis.diam@facilisisfacilisis.org","(831) 996-1240"]
        ]


print(clientes[0])

print(clientes[0][2])