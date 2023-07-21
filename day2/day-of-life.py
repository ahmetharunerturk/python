age = input("your age? ")

left_days =(90*365) - int(age)*365
left_weeks=(90*52) - int(age)*52
left_months =(90*12) - int(age)*12

print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")


