#Function definition, needs indentation for function content
def mix_ingredients():
    ingredients = ["flour", "sugar", "eggs", "milk"]
    print(f"Mixing ingredients: {ingredients}")

mix_ingredients()

#Function definition with parameter
def mixSingleIngredient(ingredient):
    print(f"Mixing ingredient: {ingredient}")

mixSingleIngredient("sugar")
mixSingleIngredient("flour")
mixSingleIngredient("eggs")

#Function definition with multiple parameters
def mixSingleIngredient(*ingredient):
    for ingredientID in ingredient:
        print(f"Mixing ingredient: {ingredientID}")

mixSingleIngredient("vanilla","sugar","flour","eggs")

#Function to receive cake orders with keywords
def placeOrder(cakeFlavor, aditionalNotes):
    print(f"Order: {cakeFlavor}. Aditional Notes: {aditionalNotes}.")

placeOrder(cakeFlavor="Red Velvet", aditionalNotes="No chips")
placeOrder("Red Velvet", "No chips")

#Functions with default values
def placeNewOrder(cakeFlavor="Chocalate", portionNumber=10):
    print(f"Order: {cakeFlavor}. Portion number: {portionNumber}.")

placeNewOrder("Red Velvet", 4)
placeNewOrder()
placeNewOrder(cakeFlavor="Strawberry")
placeNewOrder(portionNumber=15)

#Function with list as parameters
def mix_ingredients(ingredients):
    for ingredientID in ingredients:
        print(f"Mixing ingredient: {ingredientID}")


ingredients = ["flour", "sugar", "eggs", "milk","baking powder"]
mix_ingredients(ingredients)

#Return in python
def sumCalculator(num1, num2):
    return num1 + num2

print(sumCalculator(2,4))