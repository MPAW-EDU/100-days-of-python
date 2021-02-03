# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = float(weight)/(float(height)**2)
    
if bmi <= 18.5:
    bmiStatus =  "Underweight"
elif bmi > 18.5 and bmi < 24.9:
    bmiStatus = "Normal and Healthy"
elif bmi > 24.9 and bmi < 29.9:
    bmiStatus = "Overweight"
elif bmi > 29.9:
    bmiStatus = "Obese"
            


print(f"Your BMI is {bmi}, and you are {bmiStatus}.")