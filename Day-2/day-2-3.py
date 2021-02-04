# How long remains until you reach 90, days - weeks - months


# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max_age = 90;

max_time = {
    'days': max_age*365,
    'weeks': max_age*52,
    'months': max_age*12
}

current_time = {
    'days': age*365,
    'weeks': age*52,
    'months': age*12
}

remaining_time = {
    'days': max_time['days'] - current_time['days'],
    'weeks': max_time['weeks'] - current_time['weeks'],
    'months': max_time['months'] - current_time['months']
}

print(f"You have {remaining_time['days']} days, {remaining_time['weeks']} weeks, and {remaining_time['months']} months left.")


