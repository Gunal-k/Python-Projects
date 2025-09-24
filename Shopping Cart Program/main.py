#Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food=input("Enter a food to Buy (q to Quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-----YOUR CART-----")

for food,price in zip(foods,prices):
    print(f"{food}: ${price}")
    total+=price

print()
print(f"Total: ${total}")
    