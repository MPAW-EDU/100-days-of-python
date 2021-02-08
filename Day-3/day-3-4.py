# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

large = 25
medium = 20
small = 15
largeMediumPepperoni = 3
s_pepperoni = 2
extraCheese = 1

price = 0.00

if size != "S":
    if size == "L": price += large
    if size == "M": price += medium
    if add_pepperoni == "Y":
        price += largeMediumPepperoni
elif size == "S":
    price += small
    if add_pepperoni == "Y": 
        price += s_pepperoni
if extra_cheese == "Y":
    price += extraCheese

print("Your total bill will be ${:.2f}".format(price))