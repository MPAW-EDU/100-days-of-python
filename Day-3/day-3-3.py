# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if not year % 4 or year % 100 and not year % 400:
    print("Leap Year")
else:
    print("Not a Leap Year.")